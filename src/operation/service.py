from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.user.service import get_user_by_id_telegram

from . import models, schemas


async def get_operations(session: AsyncSession, id_telegram: int):
    db_user = await get_user_by_id_telegram(session, id_telegram)
    stmt = select(models.Operation).where(models.Operation.user_id == db_user.id)
    operations = await session.execute(stmt)
    return operations.scalars().all()


async def create_operation(session: AsyncSession, operation: schemas.Operation):
    new_operation = models.Operation(
        user_id=operation.user_id,
        category_user_id=operation.category_user_id,
        kind=operation.kind,
        amount=operation.amount,
    )
    session.add(new_operation)
    await session.commit()
    return new_operation
