from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api import router
from app.core.config import get_settings
from app.core.database import init_mongo_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    await init_mongo_db()
    yield


app = FastAPI(
    title=get_settings().project_name, lifespan=lifespan
)

app.include_router(router)
