import contextlib
import secrets

from sqlalchemy import select

from src.core.database import get_async_session

from .. import models

get_async_session_context = contextlib.asynccontextmanager(get_async_session)


async def create_or_update_confirm_email_token(user_id: int):
    async with get_async_session_context() as session:
        stmt = select(models.ConfirmToken).where(models.ConfirmToken.user_id == user_id)
        confirm_token = await session.execute(stmt)
        confirm_token = confirm_token.scalar()

        if confirm_token is not None:
            token = secrets.token_urlsafe(16)
            confirm_token.token = token
            session.add(confirm_token)
            await session.commit()
            await session.refresh(confirm_token)
            return token

        token = secrets.token_urlsafe(16)
        new_confirm_token = models.ConfirmToken(
            user_id=user_id,
            token=token,
        )
        session.add(new_confirm_token)
        await session.commit()

        return token
