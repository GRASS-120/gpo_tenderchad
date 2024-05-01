from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from contextlib import asynccontextmanager
import threading

from app.api import router
from app.core.config import get_settings
from app.messaging.consume import start_consume

# логика, которая происходит до запуска приложения (стоит ли тут подключать бд?)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Запускаем start_consume (принимаем сообщения rabbitmq) в отдельном потоке
    # pika запускает rabbitmq синхронно, тогда как fastapi асинхронный => rabbitmq не работает нормально
    # чтобы это исправить нужно запустить start_consume в отдельном потоке
    thread = threading.Thread(target=start_consume)
    thread.start()  
    yield
    thread.join()

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