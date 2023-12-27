from src.operation.enum import KindOperationEnum


def calc_total_user_operations(operations):
    result = 0
    for operation in operations:
        if operation.kind == KindOperationEnum(1):
            result += operation.amount
        else:
            result -= operation.amount
    return result
