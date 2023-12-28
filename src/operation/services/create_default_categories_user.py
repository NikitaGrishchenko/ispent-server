import contextlib

from src.core.config import DEFAULT_USER_OPERATION
from src.core.database import get_async_session

from .. import models

get_async_session_context = contextlib.asynccontextmanager(get_async_session)


async def create_default_categories_user(id_user: int):
    async with get_async_session_context() as session:
        for operation in DEFAULT_USER_OPERATION:
            new_category_user = models.CategoryUser(
                user_id=id_user,
                name=operation["name"],
                kind=operation["kind"],
                color=operation["color"],
                icon=operation["icon"],
            )
            session.add(new_category_user)

        await session.commit()
