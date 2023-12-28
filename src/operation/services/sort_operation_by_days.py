from src.user.services import calc_total_user_operations

from .get_operations_by_day import get_operations_by_day


def sort_operation_by_days(operations):
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
