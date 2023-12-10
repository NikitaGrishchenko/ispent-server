from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.operation.enum import KindOperationEnum
from src.operation.service import get_categories_user, get_operations

from . import models, schemas


async def get_user_by_id(session: AsyncSession, id_user: int):
    return await session.get(models.User, id_user)


async def get_user_by_id_telegram(session: AsyncSession, id_telegram: int):
    stmt = select(models.User).where(models.User.id_telegram == id_telegram)
    user = await session.execute(stmt)
    return user.scalar()


async def get_users(session: AsyncSession):
    db_users = await session.execute(select(models.User))
    return db_users.scalars().all()


def calc_total_user_operations(operations):
    result = 0
    for operation in operations:
        if operation.kind == KindOperationEnum(1):
            result += operation.amount
        else:
            result -= operation.amount
    return result


def calc_difference_user_operations(operations):
    total_income = total_expenses = 0
    for operation in operations:
        if operation.kind == KindOperationEnum(1):
            total_income += operation.amount
        else:
            total_expenses += operation.amount
    return total_income, total_expenses


def total_by_category(category, operations):
    operations_by_category = [
        operation
        for operation in operations
        if operation.category_user_id == category.id
    ]

    return calc_total_user_operations(operations_by_category)


async def get_total_by_categories(session: AsyncSession, user_id: int, operations):
    result = []
    categories_user = await get_categories_user(session, user_id)
    for index, category in enumerate(categories_user):
        result.append(
            {
                "id": index,
                "category_user": category,
                "total": total_by_category(category, operations),
            }
        )

    return [item for item in result if item.get("total") != 0]


async def get_overview_data_user(session: AsyncSession, user_id: int):
    user_operations = await get_operations(session, user_id)
    total_balance = calc_total_user_operations(user_operations)
    total_income, total_expenses = calc_difference_user_operations(user_operations)
    total_by_categories = await get_total_by_categories(
        session, user_id, user_operations
    )

    return total_balance, total_income, total_expenses, total_by_categories
