from datetime import datetime

from pydantic import BaseModel


class Operation(BaseModel):
    id: int
    user_id: int
    category: str
    kind: str
    amount: float
    date: datetime

    class Config:
        orm_mode = True
