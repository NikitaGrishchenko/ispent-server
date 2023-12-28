from sqlalchemy.ext.asyncio import AsyncSession

from .. import models


async def get_operation(session: AsyncSession, operation_id: int):
    return await session.get(models.Operation, operation_id)
