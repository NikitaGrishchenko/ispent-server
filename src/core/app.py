from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.router import api_router
from src.core.config import DOMAIN

app = FastAPI(docs_url="/api", title="ispent")


app.include_router(api_router, prefix="/api")

origins = [
    "http://localhost",
    "http://localhost:9000",
    "http://127.0.0.1:9000",
    f"https://{DOMAIN}",
    f"http://{DOMAIN}",
    f"https://www.{DOMAIN}",
    f"http://www.{DOMAIN}",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
