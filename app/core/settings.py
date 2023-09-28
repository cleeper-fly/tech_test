from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Service settings"""

    model_config = SettingsConfigDict(env_file='.app.env', env_file_encoding='utf-8')

    # App
    APP_NAME: str = 'embl-test'

    # API
    API_PREFIX: str = '/api'
    AUTO_RELOAD: bool = False
    HOST: str = '127.0.0.1'
    PORT: int = 8000
    WEB_CONCURRENCY: int = 10

    # DB
    DB_URI: str


@lru_cache
def get_settings() -> AppSettings:
    return AppSettings()
