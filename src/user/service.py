from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from . import models, schemas


async def get_user_by_id(session: AsyncSession, id_user: int):
    return await session.get(models.User, id_user)


async def get_user_by_id_telegram(session: AsyncSession, id_telegram: int):
    stmt = select(models.User).where(models.User.id_telegram == id_telegram)
    user = await session.execute(stmt)
    return user.scalar()


async def create_user(session: AsyncSession, user: schemas.User):
    # new_user = models.User(**user_in.model_dump())
    new_user = models.User(
        id_telegram=user.id_telegram,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        language_code=user.language_code,
        is_bot=user.is_bot,
        hashed_password=user.hashed_password,
    )
    session.add(new_user)
    await session.commit()
    return new_user


async def get_categories_user(session: AsyncSession, id_telegram: int):
    user = await get_user_by_id_telegram(session, id_telegram)
    categories_user = await session.execute(
        select(models.CategoryUser).where(models.CategoryUser.user_id == user.id)
    )
    return categories_user.scalars().all()


async def get_users(session: AsyncSession):
    db_users = await session.execute(select(models.User))
    return db_users.scalars().all()


async def get_category_user(session: AsyncSession, category_user: schemas.CategoryUser):
    stmt = (
        select(models.CategoryUser)
        .where(models.CategoryUser.user_id == category_user.user_id)
        .where(models.CategoryUser.name == category_user.name)
        .where(models.CategoryUser.kind == category_user.kind)
    )
    category_user = await session.execute(stmt)
    return category_user.scalar()


async def create_category_user(
    session: AsyncSession, category_user: schemas.CategoryUser
):
    new_category_user = models.CategoryUser(
        user_id=category_user.user_id,
        name=category_user.name,
        kind=category_user.kind,
    )
    session.add(new_category_user)
    await session.commit()
    return new_category_user


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
