from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

from app.api import router
from app.core.config import get_settings
from app.core.database import init_mongo_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_mongo_db()
    yield

app = FastAPI(
    title=get_settings().project_name, lifespan=lifespan
)

app.include_router(router)

def start():
    settings = get_settings()
    uvicorn.run(
        "app.main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=True
    )