from datetime import datetime
from typing import List, Union

from src.schemas import BaseSchema, SchemaResponce

from .enum import KindOperationEnum


class CategoryUser(BaseSchema):
    id: int
    user_id: int
    name: str
    kind: KindOperationEnum

    class Config:
        from_attributes = True


class Operation(BaseSchema):
    user_id: int
    category_user_id: int
    kind: KindOperationEnum
    amount: float
    date: datetime
    comment: str | None = None

    class Config:
        from_attributes = True


class OperationResponce(Operation, SchemaResponce):
    category_user: CategoryUser
