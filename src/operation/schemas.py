from datetime import datetime

from pydantic import BaseModel

from .enum import KindOperationEnum


class Operation(BaseModel):
    id: int
    user_id: int
    category_user_id: int
    kind: KindOperationEnum
    amount: float
    date: datetime

    class Config:
        from_attributes = True
