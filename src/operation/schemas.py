from datetime import datetime

from src.schemas import BaseSchema

from .enum import KindOperationEnum


class Operation(BaseSchema):
    id: int
    user_id: int
    category_user_id: int
    kind: KindOperationEnum
    amount: float
    date: datetime

    class Config:
        from_attributes = True
