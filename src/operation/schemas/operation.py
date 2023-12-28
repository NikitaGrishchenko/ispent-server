from datetime import datetime
from typing import List

from src.core.schemas import BaseSchema, SchemaResponce

from ..enum import KindOperationEnum
from .category import CategoryUserRead


class OperationBase(BaseSchema):
    category_user_id: int
    kind: KindOperationEnum
    amount: float
    comment: str | None = None
    user_id: int
    date: datetime

    class Config:
        from_attributes = True


class OperationCreate(OperationBase):
    pass


class OperationUpdate(OperationBase, SchemaResponce):
    pass


class OperationRead(OperationBase, SchemaResponce):
    category_user: CategoryUserRead


class OperationByPeriodRead(BaseSchema):
    id: int
    date: datetime
    operations: List[OperationRead]
    total: float
