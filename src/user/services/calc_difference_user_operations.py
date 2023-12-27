from src.operation.enum import KindOperationEnum


def calc_difference_user_operations(operations):
    total_income = total_expenses = 0
    for operation in operations:
        if operation.kind == KindOperationEnum(1):
            total_income += operation.amount
        else:
            total_expenses += operation.amount
    return total_income, total_expenses
