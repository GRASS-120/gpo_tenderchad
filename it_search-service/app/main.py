from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from contextlib import asynccontextmanager

from app.api import router
from app.core.config import get_settings

# логика, которая происходит до запуска приложения (стоит ли тут подключать бд?)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # сделать тут запуск цикла rabbitmq?
    yield

app = FastAPI(
    title=get_settings().project_name, lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
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