from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .. import models


async def get_operations(session: AsyncSession, user_id: int):
    stmt = select(models.Operation).where(models.Operation.user_id == user_id)
    operations = await session.execute(stmt)
    return operations.scalars().all()
