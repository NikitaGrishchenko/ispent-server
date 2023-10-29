from datetime import datetime
from typing import List

from fastapi_users import schemas

from src.operation.enum import KindOperationEnum
from src.operation.schemas import Operation
from src.schemas import BaseSchema


class User(BaseSchema):
    id: int
    id_telegram: int
    username: str | None = None
    email: str | None = None
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


class CategoryUser(BaseSchema):
    id: int
    user_id: int
    name: str
    kind: KindOperationEnum

    class Config:
        from_attributes = True


class UserRead(schemas.BaseUser[int]):
    id: int
    id_telegram: int
    username: str | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    language_code: str | None = None
    is_bot: bool | None = None
    created_at: datetime
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserCreate(schemas.BaseUserCreate):
    id: int
    id_telegram: int
    username: str | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    language_code: str | None = None
    is_bot: bool | None = None
    created_at: datetime
    password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserUpdate(schemas.BaseUserUpdate):
    pass


class OverviewUser(BaseSchema):
    total_balance: float
    total_income: float
    total_expenses: float
    # last_operations: list[Operation]

    class Config:
        from_attributes = True
