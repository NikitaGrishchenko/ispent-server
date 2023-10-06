from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session

from . import schemas, service

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


@router.get("/list/", response_model=list[schemas.User])
async def read_users(session: AsyncSession = Depends(get_async_session)):
    db_users = await service.get_users(session)
    # if db_users is None:
    #     raise HTTPException(status_code=404, detail="Users not found")
    return db_users


@router.get("/id/{id_user}", response_model=schemas.User)
async def read_user_by_id(id_user: int, db: AsyncSession = Depends(get_async_session)):
    db_user = await service.get_user_by_id(db, id_user=id_user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/id-telegram/{id_telegram}", response_model=schemas.User)
async def read_user_by_id_telegram(
    id_telegram: int, db: AsyncSession = Depends(get_async_session)
):
    db_user = await service.get_user_by_id_telegram(db, id_telegram=id_telegram)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/create/", response_model=schemas.User)
async def create_user(
    user: schemas.User, session: AsyncSession = Depends(get_async_session)
):
    new_user = service.create_user(session, user)
    await session.commit()
    return new_user

    # new_user = service.get_user_by_id_telegram(db, id_telegram=user.id_telegram)
    # if db_user:
    #     raise HTTPException(status_code=400, detail="User already registered")


@router.get("/categories/{id_telegram}", response_model=list[schemas.CategoryUser])
async def read_categories_user(
    id_telegram: int, db: AsyncSession = Depends(get_async_session)
):
    db_categories_user = await service.get_categories_user(db, id_telegram=id_telegram)
    if db_categories_user is None:
        raise HTTPException(status_code=404, detail="User categories not found")
    return db_categories_user


@router.post("/category/create/", response_model=schemas.CategoryUser)
async def create_category_user(
    category_user: schemas.CategoryUser, db: AsyncSession = Depends(get_async_session)
):
    db_category_user = await service.get_category_user(db, category_user=category_user)
    if db_category_user:
        raise HTTPException(status_code=400, detail="Category user already registered")
    return service.create_category_user(db=db, category_user=category_user)
