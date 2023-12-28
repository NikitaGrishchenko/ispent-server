from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .. import schemas
from .get_operation import get_operation


async def update_operation(
    session: AsyncSession,
    updated_data: schemas.OperationUpdate,
    current_user_id: int,
):
    stored_operation = await get_operation(session, updated_data.id)
    if stored_operation and updated_data.user_id == current_user_id:
        for key, value in updated_data.dict().items():
            setattr(stored_operation, key, value)
        await session.commit()
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Operation with id {updated_data.id} not found",
        )
    return updated_data
