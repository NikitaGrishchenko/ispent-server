from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.user import schemas, services
from src.user.auth import current_active_user
from src.user.v1.router import user_v1_router


@user_v1_router.get("/list/", response_model=list[schemas.UserRead])
async def read_users(
    user: schemas.User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    db_users = await services.get_users(session)
    return db_users
