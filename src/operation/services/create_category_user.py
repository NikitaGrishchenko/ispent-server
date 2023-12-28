from sqlalchemy.ext.asyncio import AsyncSession

from .. import models, schemas


async def create_category_user(
    session: AsyncSession, category_user: schemas.CategoryUserCreate
):
    new_category_user = models.CategoryUser(
        user_id=category_user.user_id,
        name=category_user.name,
        kind=category_user.kind,
        color=category_user.color,
        icon=category_user.icon,
    )
    session.add(new_category_user)
    await session.commit()
    return new_category_user
