from datetime import datetime

from fastapi_users import schemas

from src.core.schemas import BaseSchema


class User(BaseSchema):
    id: int
    id_telegram: int | None = None
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


class UserRead(schemas.BaseUser[int]):
    id: int
    id_telegram: int | None = None
    username: str | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    language_code: str | None = None
    is_bot: bool | None = None
    created_at: datetime
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserCreate(schemas.BaseUserCreate):
    email: str
    first_name: str | None = None
    last_name: str | None = None
    password: str


class UserUpdate(schemas.BaseUserUpdate):
    pass
