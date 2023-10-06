from datetime import datetime

from pydantic import BaseModel

from src.operation.enum import KindOperationEnum


class User(BaseModel):
    id: int
    id_telegram: int
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    language_code: str | None = None
    is_bot: bool | None = None
    created_at: datetime
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool

    class Config:
        from_attributes = True


class CategoryUser(BaseModel):
    id: int
    user_id: int
    name: str
    kind: KindOperationEnum

    class Config:
        from_attributes = True
