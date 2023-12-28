import datetime

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .. import models, schemas


async def create_operation(session: AsyncSession, operation: schemas.OperationCreate):
    if operation.date.date() > datetime.datetime.utcnow().date():
        raise HTTPException(status_code=500, detail="Incorrect date")

    new_operation = models.Operation(
        user_id=operation.user_id,
        category_user_id=operation.category_user_id,
        kind=operation.kind,
        amount=operation.amount,
        comment=operation.comment,
        date=operation.date,
    )
    session.add(new_operation)
    await session.commit()
    return new_operation
