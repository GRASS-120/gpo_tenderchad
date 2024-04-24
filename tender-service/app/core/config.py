from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    project_name: str = "Tender API"
    MONGO_HOST: str
    MONGO_PORT: str
    MONGO_USER: str
    MONGO_PASSWORD: str
    APP_HOST: str
    APP_PORT: int

    model_config = SettingsConfigDict(env_file="app/.env")


@lru_cache
def get_settings():
    return Settings()

@lru_cache
def mongo_url():
    settings = get_settings()
    return f"mongodb://{settings.MONGO_HOST}:{settings.MONGO_PORT}"