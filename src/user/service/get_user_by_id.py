from sqlalchemy.ext.asyncio import AsyncSession
from src.user import models


async def get_user_by_id(session: AsyncSession, id_user: int):
    return await session.get(models.User, id_user)
