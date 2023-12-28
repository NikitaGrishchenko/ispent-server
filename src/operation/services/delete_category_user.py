from fastapi import HTTPException
from sqlalchemy import delete, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from .. import models


async def delete_category_user(session: AsyncSession, active_user_id, id_category: int):
    stmt = select(models.CategoryUser).where(models.CategoryUser.id == id_category)
    category_user = await session.execute(stmt)
    category_user = category_user.scalar()

    # pylint: disable=E1102
    stmt = (
        select(func.count(models.Operation.id))
        .select_from(models.Operation)
        .where(models.Operation.category_user_id == category_user.id)
    )
    operations_related_category = await session.execute(stmt)

    if operations_related_category.scalar_one() > 0:
        raise HTTPException(
            status_code=500, detail="You cannot delete a category because it has links"
        )

    if category_user and category_user.user_id == active_user_id:
        stmt = delete(models.CategoryUser).where(models.CategoryUser.id == id_category)
        await session.execute(stmt)
        await session.commit()
        return category_user

    raise HTTPException(
        status_code=404, detail=f"Category user with id {active_user_id} not found"
    )
