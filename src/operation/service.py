import contextlib

from fastapi import Depends, HTTPException
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import DEFAULT_USER_OPERATION
from src.database import get_async_session

from . import models, schemas

get_async_session_context = contextlib.asynccontextmanager(get_async_session)


async def get_operations(session: AsyncSession, user_id: int):
    stmt = select(models.Operation).where(models.Operation.user_id == user_id)
    operations = await session.execute(stmt)
    return operations.scalars().all()


async def get_last_operations(session: AsyncSession, user_id: int, count: int):
    stmt = (
        select(models.Operation)
        .where(models.Operation.user_id == user_id)
        .order_by(models.Operation.id.desc())
        .limit(count)
    )
    operations = await session.execute(stmt)
    return operations.scalars().all()


async def delete_operation(session: AsyncSession, active_user_id, id_operation: int):
    stmt = select(models.Operation).where(models.Operation.id == id_operation)
    operation = await session.execute(stmt)
    operation = operation.scalar()

    if operation and operation.user_id == active_user_id:
        stmt = delete(models.Operation).where(models.Operation.id == id_operation)
        await session.execute(stmt)
        await session.commit()
    else:
        raise HTTPException(
            status_code=404, detail=f"Операция с id {active_user_id} не найдена"
        )


async def create_operation(session: AsyncSession, operation: schemas.Operation):
    new_operation = models.Operation(
        user_id=operation.user_id,
        category_user_id=operation.category_user_id,
        kind=operation.kind,
        amount=operation.amount,
        comment=operation.comment,
    )
    session.add(new_operation)
    await session.commit()
    return new_operation


async def update_operation(session: AsyncSession, operation: schemas.Operation):
    # stored_item_data = items[item_id]
    # stored_item_model = Item(**stored_item_data)
    # update_data = item.dict(exclude_unset=True)
    # updated_item = stored_item_model.copy(update=update_data)
    # items[item_id] = jsonable_encoder(updated_item)

    new_operation = models.Operation(
        user_id=operation.user_id,
        category_user_id=operation.category_user_id,
        kind=operation.kind,
        amount=operation.amount,
        comment=operation.comment,
    )
    session.add(new_operation)
    await session.commit()
    return new_operation


async def get_category_user(session: AsyncSession, category_user: schemas.CategoryUser):
    stmt = (
        select(models.CategoryUser)
        .where(models.CategoryUser.user_id == category_user.user_id)
        .where(models.CategoryUser.name == category_user.name)
        .where(models.CategoryUser.kind == category_user.kind)
    )
    category_user = await session.execute(stmt)
    return category_user.scalar()


async def create_category_user(
    session: AsyncSession, category_user: schemas.CategoryUser
):
    new_category_user = models.CategoryUser(
        user_id=category_user.user_id,
        name=category_user.name,
        kind=category_user.kind,
    )
    session.add(new_category_user)
    await session.commit()
    return new_category_user


async def get_categories_user(session: AsyncSession, user_id: int):
    categories_user = await session.execute(
        select(models.CategoryUser).where(models.CategoryUser.user_id == user_id)
    )
    return categories_user.scalars().all()


async def create_default_categories_user(id_user: int):
    async with get_async_session_context() as session:
        for operation in DEFAULT_USER_OPERATION:
            new_category_user = models.CategoryUser(
                user_id=id_user,
                name=operation["name"],
                kind=operation["kind"],
            )
            session.add(new_category_user)

        await session.commit()
