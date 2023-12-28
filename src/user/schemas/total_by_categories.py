from src.core.schemas import SchemaResponce
from src.operation.schemas import CategoryUserRead


class TotalByCategories(SchemaResponce):
    category_user: CategoryUserRead
    total: float
