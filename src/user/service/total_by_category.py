from .calc_total_user_operations import calc_total_user_operations


def total_by_category(category, operations):
    operations_by_category = [
        operation
        for operation in operations
        if operation.category_user_id == category.id
    ]

    return calc_total_user_operations(operations_by_category)
