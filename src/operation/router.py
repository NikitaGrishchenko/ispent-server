from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.user.auth import current_active_user
from src.user.schemas import User

from . import schemas, service

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


@router.get("/list/", response_model=list[schemas.OperationResponce])
async def read_operations(
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    operations = await service.get_operations(session, user.id)
    return operations


@router.post("/create/", response_model=schemas.Operation)
async def create_operation(
    operation: schemas.Operation,
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    return await service.create_operation(session, operation)


@router.delete("/delete/{id_operation}")
async def delete_operation(
    id_operation: int,
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    return await service.delete_operation(session, user.id, id_operation)


@router.get("/categories/", response_model=list[schemas.CategoryUser])
async def read_categories_user(
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    categories_user = await service.get_categories_user(session, user.id)
    return categories_user


@router.post("/category/create/", response_model=schemas.CategoryUser)
async def create_category_user(
    category_user: schemas.CategoryUser,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user),
):
    db_category_user = await service.get_category_user(session, category_user)
    if db_category_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User category already exists",
        )
    return await service.create_category_user(session, category_user)
