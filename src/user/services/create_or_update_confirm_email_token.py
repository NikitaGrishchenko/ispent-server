import contextlib
import secrets

from src.core.database import get_async_session

from .. import models
from .get_user_by_id import get_user_by_id

get_async_session_context = contextlib.asynccontextmanager(get_async_session)


async def create_or_update_confirm_email_token(user_id: int):
    async with get_async_session_context() as session:
        token = secrets.token_urlsafe(16)
        new_confirm_token = models.ConfirmToken(
            user_id=user_id,
            token=token,
        )
        session.add(new_confirm_token)

        await session.commit()

    return token
