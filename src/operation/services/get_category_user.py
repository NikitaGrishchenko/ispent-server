from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .. import models


async def get_category_user(session: AsyncSession, category_user_id: int):
    stmt = select(models.CategoryUser).where(models.CategoryUser.id == category_user_id)
    category_user = await session.execute(stmt)
    return category_user.scalar()
