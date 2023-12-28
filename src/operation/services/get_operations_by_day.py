def get_operations_by_day(date, operations):
    operations = [
        operation for operation in operations if operation.date.date() == date
    ]
    return sorted(operations, key=lambda x: x.id, reverse=True)
