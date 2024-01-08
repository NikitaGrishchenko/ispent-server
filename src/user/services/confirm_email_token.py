from fastapi import HTTPException
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_async_session

from .. import models
from .get_user_by_id import get_user_by_id


async def confirm_email_token(session: AsyncSession, token: str, user_id: int):
    stmt = (
        select(models.ConfirmToken)
        .where(models.ConfirmToken.user_id == user_id)
        .where(models.ConfirmToken.token == token)
    )
    confirm_token = await session.execute(stmt)
    confirm_token = confirm_token.scalar()

    if confirm_token:
        user = await get_user_by_id(session, user_id)
        user.is_verified = True
        session.add(user)
        await session.commit()
        await session.refresh(user)

        stmt = delete(models.ConfirmToken).where(
            models.ConfirmToken.id == confirm_token.id
        )
        await session.execute(stmt)
        await session.commit()
        return user

    raise HTTPException(status_code=404, detail="Invalid token")
