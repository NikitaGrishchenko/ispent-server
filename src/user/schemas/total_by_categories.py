from src.operation.schemas import CategoryUserRead
from src.schemas import SchemaResponce


class TotalByCategories(SchemaResponce):
    category_user: CategoryUserRead
    total: float
