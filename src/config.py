import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = str(os.getenv("TOKEN"))

DATABASE_URL = str(os.getenv("DATABASE_URL"))

DOCKER_DB_NAME = str(os.getenv("DOCKER_DB_NAME"))
DOCKER_DB_USER = str(os.getenv("DOCKER_DB_USER"))
DOCKER_DB_PASSWORD = str(os.getenv("DOCKER_DB_PASSWORD"))
DOCKER_DB_HOST = str(os.getenv("DOCKER_DB_HOST"))


DEFAULT_USER_OPERATION = [
    {
        "kind": 0,
        "name": "Продукты",
    },
    {
        "kind": 0,
        "name": "Развлечения",
    },
    {
        "kind": 0,
        "name": "Прочее",
    },
    {
        "kind": 1,
        "name": "Зарплата",
    },
    {
        "kind": 1,
        "name": "Пассивный доход",
    },
    {
        "kind": 1,
        "name": "Прочее",
    },
]
