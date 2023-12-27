from sqlalchemy.ext.asyncio import AsyncSession

from src.operation.service import get_categories_user

from .total_by_category import total_by_category


async def get_total_by_categories(session: AsyncSession, user_id: int, operations):
    result = []
    categories_user = await get_categories_user(session, user_id)
    for index, category in enumerate(categories_user):
        result.append(
            {
                "id": index,
                "category_user": category,
                "total": total_by_category(category, operations),
            }
        )

    return [item for item in result if item.get("total") != 0]
