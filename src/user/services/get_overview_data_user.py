from sqlalchemy.ext.asyncio import AsyncSession

from src.operation import services

from .calc_difference_user_operations import calc_difference_user_operations
from .calc_total_user_operations import calc_total_user_operations
from .get_total_by_categories import get_total_by_categories


async def get_overview_data_user(session: AsyncSession, user_id: int):
    user_operations = await services.get_operations_for_period_of_time(
        session, user_id, None, None
    )
    total_balance = calc_total_user_operations(user_operations)
    total_income, total_expenses = calc_difference_user_operations(user_operations)
    total_by_categories = await get_total_by_categories(
        session, user_id, user_operations
    )

    return total_balance, total_income, total_expenses, total_by_categories
