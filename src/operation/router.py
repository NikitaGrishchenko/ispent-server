from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session

from . import schemas, service

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


@router.get("/{id_telegram}", response_model=list[schemas.Operation])
def read_operations(id_telegram: int, db: AsyncSession = Depends(get_async_session)):
    db_operations = service.get_operations(db, id_telegram)
    if db_operations is None:
        raise HTTPException(status_code=404, detail="Operations not found")
    return db_operations


# @router.get("/{id_operation}", response_model=schemas.Operation)
# def read_operation(id_operation: int, db: Session = Depends(get_db)):
#     db_operation = service.get_operation(db, id_user=id_user)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


@router.post("/create/", response_model=schemas.Operation)
def create_operation(
    operation: schemas.Operation, db: AsyncSession = Depends(get_async_session)
):
    return service.create_operation(db=db, operation=operation)
