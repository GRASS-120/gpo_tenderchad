from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    project_name: str = "ItAnalysisService"
    APP_HOST: str
    APP_PORT: int

    model_config = SettingsConfigDict(env_file="app/.env")

@lru_cache
def get_settings():
    return Settings()