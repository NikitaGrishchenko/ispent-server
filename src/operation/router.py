from fastapi import APIRouter

router = APIRouter()

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


@router.get("/list")
async def get_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/{user_id}")
async def get_user(user_id: int):
    return [{"username": "Rick"}]
