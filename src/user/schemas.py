from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    id_telegram: int
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    language_code: str | None = None
    is_bot: bool | None = None
    created_at: datetime

    class Config:
        orm_mode = True


class CategoryUser(BaseModel):
    id: int
    user_id: int
    name: str
    kind: str

    class Config:
        orm_mode = True
