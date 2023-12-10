import calendar
import contextlib
import datetime
from pprint import pprint

from fastapi import Depends, HTTPException
from sqlalchemy import delete, desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import DEFAULT_USER_OPERATION
from src.database import get_async_session

from . import models, schemas

get_async_session_context = contextlib.asynccontextmanager(get_async_session)


async def get_operations(session: AsyncSession, user_id: int):
    stmt = select(models.Operation).where(models.Operation.user_id == user_id)
    operations = await session.execute(stmt)
    return operations.scalars().all()


def get_start_and_end_of_current_month():
    today = datetime.datetime.today()

    starting_date = today.replace(
        day=1,
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
    )
    end_date = today.replace(
        day=calendar.monthrange(today.year, today.month)[1],
        hour=23,
        minute=59,
        second=59,
        microsecond=999999,
    )
    return starting_date, end_date


def get_operations_by_day(date, operations):
    operations = [
        operation for operation in operations if operation.date.date() == date
    ]
    return sorted(operations, key=lambda x: x.id, reverse=True)


def sort_operation_by_days(operations):
    from src.user.service import calc_total_user_operations

    days = []
    for operation in operations:
        if operation.date not in days:
            days.append(operation.date)

    result = []
    days.sort()

    for index, day in enumerate(days):
        operations_by_day = get_operations_by_day(day.date(), operations)
        result.append(
            {
                "id": index,
                "date": day.date(),
                "operations": operations_by_day,
                "total": calc_total_user_operations(operations_by_day),
            }
        )

    return result


async def get_operations_for_period_of_time(
    session: AsyncSession,
    user_id: int,
    starting_date: str,
    end_date: str,
):
    if starting_date is None and end_date is None:
        starting_date, end_date = get_start_and_end_of_current_month()

    stmt = (
        select(models.Operation)
        .where(models.Operation.user_id == user_id)
        .where(models.Operation.date >= starting_date)
        .where(models.Operation.date <= end_date)
    )
    operations_db = await session.execute(stmt)

    return sort_operation_by_days(operations_db.scalars().all())


async def get_operation(session: AsyncSession, operation_id: int):
    return await session.get(models.Operation, operation_id)


async def get_last_operations(session: AsyncSession, user_id: int, count: int):
    stmt = (
        select(models.Operation)
        .where(models.Operation.user_id == user_id)
        .order_by(models.Operation.date.desc())
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
        return operation

    raise HTTPException(
        status_code=404, detail=f"Operation with id {active_user_id} not found"
    )


async def create_operation(session: AsyncSession, operation: schemas.OperationCreate):
    if operation.date.date() > datetime.datetime.utcnow().date():
        raise HTTPException(status_code=500, detail="Incorrect date")

    new_operation = models.Operation(
        user_id=operation.user_id,
        category_user_id=operation.category_user_id,
        kind=operation.kind,
        amount=operation.amount,
        comment=operation.comment,
        date=operation.date,
    )
    session.add(new_operation)
    await session.commit()
    return new_operation


async def update_operation(
    session: AsyncSession,
    updated_data: schemas.OperationUpdate,
    current_user_id: int,
):
    stored_operation = await get_operation(session, updated_data.id)
    if stored_operation and updated_data.user_id == current_user_id:
        for key, value in updated_data.dict().items():
            setattr(stored_operation, key, value)
        await session.commit()
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Operation with id {updated_data.id} not found",
        )
    return updated_data


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


async def get_category_user(session: AsyncSession, category_user_id: int):
    stmt = select(models.CategoryUser).where(models.CategoryUser.id == category_user_id)
    category_user = await session.execute(stmt)
    return category_user.scalar()


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


async def get_categories_user(session: AsyncSession, user_id: int):
    categories_user = await session.execute(
        select(models.CategoryUser)
        .where(models.CategoryUser.user_id == user_id)
        .order_by(desc("id"))
    )
    return categories_user.scalars().all()


async def create_default_categories_user(id_user: int):
    async with get_async_session_context() as session:
        for operation in DEFAULT_USER_OPERATION:
            new_category_user = models.CategoryUser(
                user_id=id_user,
                name=operation["name"],
                kind=operation["kind"],
                color=operation["color"],
                icon=operation["icon"],
            )
            session.add(new_category_user)

        await session.commit()


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


async def update_category_user(
    session: AsyncSession,
    updated_data: schemas.CategoryUserUpdate,
    current_user_id: int,
):
    stored_category_user = await get_category_user(session, updated_data.id)
    if stored_category_user and updated_data.user_id == current_user_id:
        for key, value in updated_data.dict().items():
            setattr(stored_category_user, key, value)
        await session.commit()
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Category user with id {updated_data.id} not found",
        )
    return updated_data
