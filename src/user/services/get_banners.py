from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.user import models


async def get_banners(session: AsyncSession, user):
    banners = []

    if user.is_verified is False:
        banners.append(
            {
                "id": 1,
                "text": "A confirmation email has been sent to your email address",
                "icon": "new_releases",
                "color": "red-4",
            }
        )

    return banners
