from sqlalchemy.orm import Session

from src.user.service import get_user_by_id_telegram

from . import models, schemas


def get_operations(db: Session, id_telegram: int):
    db_user = get_user_by_id_telegram(db, id_telegram)
    return (
        db.query(models.Operation).filter(models.Operation.user_id == db_user.id).all()
    )


def create_operation(db: Session, operation: schemas.Operation):
    db_operation = models.Operation(
        user_id=operation.user_id,
        category_user_id=operation.category_user_id,
        kind=operation.kind,
        amount=operation.amount,
    )
    db.add(db_operation)
    db.commit()
    db.refresh(db_operation)
    return db_operation
