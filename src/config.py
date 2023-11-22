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
        "icon": "shopping_basket",
        "color": "#109715",
    },
    {
        "kind": "EXPENSE",
        "name": "Развлечения",
        "icon": "nightlife",
        "color": "#6C1097",
    },
    {
        "kind": "EXPENSE",
        "name": "Обед",
        "icon": "restaurant",
        "color": "#E6EA1E",
    },
    {
        "kind": "EXPENSE",
        "name": "Прочий расход",
        "icon": "radio_button_unchecked",
        "color": "#1E87C2",
    },
    {
        "kind": "INCOME",
        "name": "Зарплата",
        "icon": "payments",
        "color": "#64EB81",
    },
    {
        "kind": "INCOME",
        "name": "Пассивный доход",
        "icon": "account_balance_wallet",
        "color": "#D3A223",
    },
    {
        "kind": "INCOME",
        "name": "Прочий доход",
        "icon": "radio_button_unchecked",
        "color": "#CD2375",
    },
]
