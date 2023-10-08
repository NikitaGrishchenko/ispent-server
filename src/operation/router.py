from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.user.auth import current_active_user
from src.user.schemas import User

from . import schemas, service

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


@router.get("/list/", response_model=list[schemas.Operation])
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
