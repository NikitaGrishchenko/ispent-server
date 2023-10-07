from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session

from . import schemas, service

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


@router.get("/{id_telegram}", response_model=list[schemas.Operation])
async def read_operations(
    id_telegram: int, session: AsyncSession = Depends(get_async_session)
):
    operations = await service.get_operations(session, id_telegram)
    return operations


@router.post("/create/", response_model=schemas.Operation)
async def create_operation(
    operation: schemas.Operation, session: AsyncSession = Depends(get_async_session)
):
    return await service.create_operation(session, operation)
