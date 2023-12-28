from fastapi import HTTPException
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from .. import models


async def delete_operation(session: AsyncSession, active_user_id, id_operation: int):
    stmt = select(models.Operation).where(models.Operation.id == id_operation)
    operation = await session.execute(stmt)
    operation = operation.scalar()

    if operation and operation.user_id == active_user_id:
        stmt = delete(models.Operation).where(models.Operation.id == id_operation)
        await session.execute(stmt)
        await session.commit()
        return operation

    raise HTTPException(
        status_code=404, detail=f"Operation with id {active_user_id} not found"
    )
