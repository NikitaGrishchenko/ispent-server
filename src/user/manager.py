import re
from typing import Optional

from fastapi import Depends, HTTPException, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions, models
from fastapi_users.db import SQLAlchemyUserDatabase

from src.core.config import SECRET
from src.core.database import get_user_db
from src.operation.services import create_default_categories_user
from src.user.models import User

from .schemas import UserCreate
from .services import send_user_confirm_email


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        await create_default_categories_user(user.id)
        await send_user_confirm_email(user)

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")

    def validate_email(self, email: str):
        pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
        if not re.match(pattern, email):
            raise HTTPException(status_code=500, detail="Incorrect email")

    async def create(
        self,
        user_create: UserCreate,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        await self.validate_password(user_create.password, user_create)

        self.validate_email(user_create.email)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()
        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )

        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)
