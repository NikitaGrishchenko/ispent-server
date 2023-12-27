from fastapi import FastAPI

from src.api.router import api_router

app = FastAPI(docs_url="/api", title="ispent")


app.include_router(api_router, prefix="/api")
