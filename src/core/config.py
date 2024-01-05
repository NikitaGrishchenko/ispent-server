import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi_mail import ConnectionConfig

load_dotenv()

TOKEN = str(os.getenv("TOKEN"))

DATABASE_URL = str(os.getenv("DATABASE_URL"))

SECRET = str(os.getenv("SECRET"))
DOMAIN = str(os.getenv("DOMAIN", default="localhost"))

DOCKER_DB_NAME = str(os.getenv("DOCKER_DB_NAME"))
DOCKER_DB_USER = str(os.getenv("DOCKER_DB_USER"))
DOCKER_DB_PASSWORD = str(os.getenv("DOCKER_DB_PASSWORD"))
DOCKER_DB_HOST = str(os.getenv("DOCKER_DB_HOST"))
DOCKER_DB_PORT = str(os.getenv("DOCKER_DB_PORT"))


SMTP_USERNAME = str(os.getenv("SMTP_USERNAME"))
SMTP_PASSWORD = str(os.getenv("SMTP_PASSWORD"))
SMTP_FROM = str(os.getenv("SMTP_FROM"))
SMTP_PORT = str(os.getenv("SMTP_PORT"))
SMTP_SERVER = str(os.getenv("SMTP_SERVER"))
SMTP_FROM_NAME = str(os.getenv("SMTP_FROM_NAME"))


SMTP_CONFIG = ConnectionConfig(
    MAIL_USERNAME=SMTP_USERNAME,
    MAIL_PASSWORD=SMTP_PASSWORD,
    MAIL_FROM=SMTP_FROM,
    MAIL_PORT=SMTP_PORT,
    MAIL_SERVER=SMTP_SERVER,
    MAIL_FROM_NAME=SMTP_FROM_NAME,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    TEMPLATE_FOLDER=Path(__file__).parent / "templates",
)


DEFAULT_USER_OPERATION = [
    {
        "kind": "EXPENSE",
        "name": "Products",
        "icon": "shopping_basket",
        "color": "#109715",
    },
    {
        "kind": "EXPENSE",
        "name": "Entertainment",
        "icon": "nightlife",
        "color": "#6C1097",
    },
    {
        "kind": "EXPENSE",
        "name": "Dinner",
        "icon": "restaurant",
        "color": "#E6EA1E",
    },
    {
        "kind": "EXPENSE",
        "name": "Other expenses",
        "icon": "radio_button_unchecked",
        "color": "#1E87C2",
    },
    {
        "kind": "INCOME",
        "name": "Salary",
        "icon": "payments",
        "color": "#64EB81",
    },
    {
        "kind": "INCOME",
        "name": "Passive income",
        "icon": "account_balance_wallet",
        "color": "#D3A223",
    },
    {
        "kind": "INCOME",
        "name": "Other income",
        "icon": "radio_button_unchecked",
        "color": "#CD2375",
    },
]
