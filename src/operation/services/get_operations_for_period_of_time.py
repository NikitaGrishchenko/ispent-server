from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .. import models
from .get_start_and_end_of_current_month import get_start_and_end_of_current_month
from .sort_operation_by_days import sort_operation_by_days


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
    return operations_db.scalars().all()
