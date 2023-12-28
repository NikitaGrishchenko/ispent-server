from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from .. import models


async def get_categories_user(session: AsyncSession, user_id: int):
    categories_user = await session.execute(
        select(models.CategoryUser)
        .where(models.CategoryUser.user_id == user_id)
        .order_by(desc("id"))
    )
    return categories_user.scalars().all()
