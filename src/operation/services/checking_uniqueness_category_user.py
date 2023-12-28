from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .. import models, schemas


async def checking_uniqueness_category_user(
    session: AsyncSession, category_user: schemas.CategoryUserRead
):
    stmt = (
        select(models.CategoryUser)
        .where(models.CategoryUser.user_id == category_user.user_id)
        .where(models.CategoryUser.name == category_user.name)
        .where(models.CategoryUser.kind == category_user.kind)
    )
    category_user = await session.execute(stmt)
    return category_user.scalar()
