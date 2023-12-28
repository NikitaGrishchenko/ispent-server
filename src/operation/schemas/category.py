from src.core.schemas import BaseSchema, SchemaResponce

from ..enum import KindOperationEnum


class CategoryUserBase(BaseSchema):
    user_id: int
    name: str
    color: str
    icon: str
    kind: KindOperationEnum

    class Config:
        from_attributes = True


class CategoryUserCreate(CategoryUserBase):
    pass


class CategoryUserRead(CategoryUserBase, SchemaResponce):
    pass


class CategoryUserUpdate(CategoryUserBase, SchemaResponce):
    pass
