from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session

from . import schemas, service
from .auth import current_active_user

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


@router.get("/list/", response_model=list[schemas.User])
async def read_users(
    user: schemas.User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    db_users = await service.get_users(session)
    return db_users


@router.get("/{id_user}", response_model=schemas.User)
async def read_user_by_id(
    id_user: int,
    user: schemas.User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    user = await service.get_user_by_id(session, id_user)
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User {id_user} not found",
    )


@router.get("/id-telegram/{id_telegram}", response_model=schemas.User)
async def read_user_by_id_telegram(
    id_telegram: int,
    user: schemas.User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    user = await service.get_user_by_id_telegram(session, id_telegram)
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User {id_telegram} not found",
    )


@router.get("/categories/", response_model=list[schemas.CategoryUser])
async def read_categories_user(
    user: schemas.User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    categories_user = await service.get_categories_user(session, user.id)
    return categories_user


@router.post("/category/create/", response_model=schemas.CategoryUser)
async def create_category_user(
    category_user: schemas.CategoryUser,
    session: AsyncSession = Depends(get_async_session),
    user: schemas.User = Depends(current_active_user),
):
    db_category_user = await service.get_category_user(session, category_user)
    if db_category_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User category already exists",
        )
    return await service.create_category_user(session, category_user)


@router.get("/overview/", response_model=schemas.OverviewUser)
async def read_overview_user(
    user: schemas.User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    (
        total_balance,
        monthly_income,
        monthly_expenses,
    ) = await service.get_overview_data_user(session, user.id)

    return {
        "total_balance": total_balance,
        "monthly_income": monthly_income,
        "monthly_expenses": monthly_expenses,
    }
