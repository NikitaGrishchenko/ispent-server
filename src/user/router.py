from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db

from . import schemas, service

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


@router.get("/{user_id}", response_model=schemas.User)
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = service.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/create/", response_model=schemas.User)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    db_user = service.get_user_by_id_telegram(db, id_telegram=user.id_telegram)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return service.create_user(db=db, user=user)
