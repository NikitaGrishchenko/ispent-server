from datetime import datetime
from typing import List, Union

from src.schemas import BaseSchema, SchemaResponce

from .enum import KindOperationEnum


class CategoryUserBase(BaseSchema):
    user_id: int
    name: str
    color: str
    icon: str
    kind: KindOperationEnum

    class Config:
        from_attributes = True


class CategoryUserCreate(CategoryUserBase):
    pass


class CategoryUserRead(CategoryUserBase, SchemaResponce):
    pass


class CategoryUserUpdate(CategoryUserBase, SchemaResponce):
    pass


class OperationBase(BaseSchema):
    category_user_id: int
    kind: KindOperationEnum
    amount: float
    comment: str | None = None
    user_id: int

    class Config:
        from_attributes = True


class OperationCreate(OperationBase):
    pass


class OperationUpdate(OperationBase, SchemaResponce):
    pass


class OperationRead(OperationBase, SchemaResponce):
    category_user: CategoryUserRead
    date: datetime
