from sqlalchemy.ext.asyncio import AsyncSession

from src.operation.services import get_operations

from .calc_difference_user_operations import calc_difference_user_operations
from .calc_total_user_operations import calc_total_user_operations
from .get_total_by_categories import get_total_by_categories


async def get_overview_data_user(session: AsyncSession, user_id: int):
    user_operations = await get_operations(session, user_id)
    total_balance = calc_total_user_operations(user_operations)
    total_income, total_expenses = calc_difference_user_operations(user_operations)
    total_by_categories = await get_total_by_categories(
        session, user_id, user_operations
    )

    return total_balance, total_income, total_expenses, total_by_categories
