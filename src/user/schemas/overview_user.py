from src.core.schemas import BaseSchema
from src.operation.schemas import OperationRead

from .total_by_categories import TotalByCategories


class OverviewUser(BaseSchema):
    total_balance: float
    total_income: float
    total_expenses: float
    last_operations: list[OperationRead]
    total_by_categories: list[TotalByCategories]

    class Config:
        from_attributes = True
