from datetime import datetime

from pydantic import BaseModel


class Operation(BaseModel):
    id: int
    user_id: int
    category_user_id: int
    kind: str
    amount: float
    date: datetime

    class Config:
        orm_mode = True
