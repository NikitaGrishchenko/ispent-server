from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .. import schemas
from .get_category_user import get_category_user


async def update_category_user(
    session: AsyncSession,
    updated_data: schemas.CategoryUserUpdate,
    current_user_id: int,
):
    stored_category_user = await get_category_user(session, updated_data.id)
    if stored_category_user and updated_data.user_id == current_user_id:
        for key, value in updated_data.dict().items():
            setattr(stored_category_user, key, value)
        await session.commit()
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Category user with id {updated_data.id} not found",
        )
    return updated_data
