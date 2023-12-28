from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_async_session
from src.operation.services import get_last_operations
from src.user import schemas, services
from src.user.auth import current_active_user

router = APIRouter()


@router.get("/list/", response_model=list[schemas.UserRead])
async def read_users(
    user: schemas.User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    db_users = await services.get_users(session)
    return db_users


@router.get("/{id_user}", response_model=schemas.UserRead)
async def read_user_by_id(
    id_user: int,
    user: schemas.User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    current_user = await services.get_user_by_id(session, id_user)
    if current_user is not None:
        return current_user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User {id_user} not found",
    )


@router.get("/id-telegram/{id_telegram}", response_model=schemas.UserRead)
async def read_user_by_id_telegram(
    id_telegram: int,
    user: schemas.User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    current_user = await services.get_user_by_id_telegram(session, id_telegram)
    if current_user is not None:
        return current_user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User {id_telegram} not found",
    )


@router.get("/overview/", response_model=schemas.OverviewUser)
async def read_overview_user(
    user: schemas.User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    (
        total_balance,
        total_income,
        total_expenses,
        total_by_categories,
    ) = await services.get_overview_data_user(session, user.id)
    last_operations = await get_last_operations(session, user.id, 5)

    return {
        "total_balance": total_balance,
        "total_income": total_income,
        "total_expenses": total_expenses,
        "last_operations": last_operations,
        "total_by_categories": total_by_categories,
    }
