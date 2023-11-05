from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.operation.enum import KindOperationEnum
from src.operation.service import get_operations

from . import models, schemas


async def get_user_by_id(session: AsyncSession, id_user: int):
    return await session.get(models.User, id_user)


async def get_user_by_id_telegram(session: AsyncSession, id_telegram: int):
    stmt = select(models.User).where(models.User.id_telegram == id_telegram)
    user = await session.execute(stmt)
    return user.scalar()


# async def create_user(session: AsyncSession, user: schemas.User):
#     # new_user = models.User(**user_in.model_dump())
#     new_user = models.User(
#         id_telegram=user.id_telegram,
#         username=user.username,
#         first_name=user.first_name,
#         last_name=user.last_name,
#         language_code=user.language_code,
#         is_bot=user.is_bot,
#         # hashed_password=get_user_manager.password_helper.hash(user.password),
#         email="nikita",
#     )
#     session.add(new_user)
#     await session.commit()
#     return new_user


async def get_users(session: AsyncSession):
    db_users = await session.execute(select(models.User))
    return db_users.scalars().all()


def calc_total_user_operations(operations):
    result = 0
    for operation in operations:
        if operation.kind == KindOperationEnum(1):
            result += operation.amount
        else:
            result -= operation.amount
    return result


def calc_difference_user_operations(operations):
    total_income = total_expenses = 0
    for operation in operations:
        if operation.kind == KindOperationEnum(1):
            total_income += operation.amount
        else:
            total_expenses += operation.amount
    return total_income, total_expenses


async def get_overview_data_user(session: AsyncSession, user_id: int):
    user_operations = await get_operations(session, user_id)
    total_balance = calc_total_user_operations(user_operations)
    total_income, total_expenses = calc_difference_user_operations(user_operations)
    # categories_user = await session.execute(
    #     select(models.CategoryUser).where(models.CategoryUser.user_id == user_id)
    # )

    return total_balance, total_income, total_expenses


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
