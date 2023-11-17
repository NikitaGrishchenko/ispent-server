import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = str(os.getenv("TOKEN"))

DATABASE_URL = str(os.getenv("DATABASE_URL"))

SECRET = str(os.getenv("SECRET"))

DOCKER_DB_NAME = str(os.getenv("DOCKER_DB_NAME"))
DOCKER_DB_USER = str(os.getenv("DOCKER_DB_USER"))
DOCKER_DB_PASSWORD = str(os.getenv("DOCKER_DB_PASSWORD"))
DOCKER_DB_HOST = str(os.getenv("DOCKER_DB_HOST"))
DOCKER_DB_PORT = str(os.getenv("DOCKER_DB_PORT"))


DEFAULT_USER_OPERATION = [
    {
        "kind": "EXPENSE",
        "name": "Продукты",
    },
    {
        "kind": "EXPENSE",
        "name": "Развлечения",
    },
    {
        "kind": "EXPENSE",
        "name": "Прочее",
    },
    {
        "kind": "INCOME",
        "name": "Зарплата",
    },
    {
        "kind": "INCOME",
        "name": "Пассивный доход",
    },
    {
        "kind": "INCOME",
        "name": "Прочее",
    },
]
