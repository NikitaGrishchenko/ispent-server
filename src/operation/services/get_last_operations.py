from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .. import models


async def get_last_operations(session: AsyncSession, user_id: int, count: int):
    stmt = (
        select(models.Operation)
        .where(models.Operation.user_id == user_id)
        .order_by(models.Operation.date.desc())
        .order_by(models.Operation.id.desc())
        .limit(count)
    )
    operations = await session.execute(stmt)
    return operations.scalars().all()
