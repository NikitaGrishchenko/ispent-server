from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.user import models


async def get_user_by_id_telegram(session: AsyncSession, id_telegram: int):
    stmt = select(models.User).where(models.User.id_telegram == id_telegram)
    user = await session.execute(stmt)
    return user.scalar()
