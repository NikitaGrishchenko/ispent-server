from fastapi import APIRouter

router = APIRouter()

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/{user_id}")
async def get_user(user_id: int):
    return [{"username": "Rick"}]
