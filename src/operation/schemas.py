from datetime import datetime

from src.schemas import BaseSchema, SchemaResponce

from .enum import KindOperationEnum


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
    pass
