from pathlib import Path
from os import getenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    app_name: str
    debug: bool
    db_url: str
    secret_key: str
    db_echo: bool = True
    # db_echo: bool = False #должен быть false режим отладки

    environment: str = "development"
    access_token_expire_minutes: int = 30
    redis_url: str = "redis://localhost:6379/0"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        env_ignore_empty=True,
    )


settings = Settings()
# .
