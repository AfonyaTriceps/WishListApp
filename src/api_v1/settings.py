from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

env_file = f'{Path(__file__).parent.parent.parent}/.env'


class Settings(BaseSettings):
    """Класс настроек приложения"""
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: str
    DB_HOST: str

    RESET_PASSWORD_TOKEN_SECRET: str
    VERIFICATION_TOKEN_SECRET: str

    api_v1_prefix: str = '/api/v1'
    auth_prefix: str = f'{api_v1_prefix[1:]}/auth/login'

    model_config = SettingsConfigDict(env_file=env_file, env_file_encoding='utf-8', extra='ignore')

    @property
    def db_url(self) -> str:
        """Возвращает URL для подключения к базе данных"""
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


settings = Settings()
