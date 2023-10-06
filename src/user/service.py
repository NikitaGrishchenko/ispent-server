from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from . import models, schemas


def get_user_by_id(db: AsyncSession, id_user: int):
    return db.query(models.User).filter(models.User.id == id_user).first()


def get_user_by_id_telegram(db: AsyncSession, id_telegram: int):
    return db.query(models.User).filter(models.User.id_telegram == id_telegram).first()


def create_user(session: AsyncSession, user: schemas.User):
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
    return new_user


def get_categories_user(db: AsyncSession, id_telegram: int):
    db_user = get_user_by_id_telegram(db, id_telegram)
    return (
        db.query(models.CategoryUser)
        .filter(models.CategoryUser.user_id == db_user.id)
        .all()
    )


async def get_users(session: AsyncSession):
    db_users = await session.execute(select(models.User))
    return db_users.scalars().all()


def get_category_user(db: AsyncSession, category_user: schemas.CategoryUser):
    return (
        db.query(models.CategoryUser)
        .filter(models.CategoryUser.user_id == category_user.user_id)
        .filter(models.CategoryUser.name == category_user.name)
        .filter(models.CategoryUser.kind == category_user.kind)
        .first()
    )


def create_category_user(db: AsyncSession, category_user: schemas.CategoryUser):
    db_category_user = models.CategoryUser(
        user_id=category_user.user_id,
        name=category_user.name,
        kind=category_user.kind,
    )
    db.add(db_category_user)
    db.commit()
    db.refresh(db_category_user)
    return db_category_user


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
