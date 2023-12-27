from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.user import models


async def get_users(session: AsyncSession):
    db_users = await session.execute(select(models.User))
    return db_users.scalars().all()
