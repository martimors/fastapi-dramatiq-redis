from pydantic import BaseSettings
from pydantic import RedisDsn


class Settings(BaseSettings):
    REDIS_DSN: RedisDsn = "redis://localhost/0"  # type: ignore


settings = Settings()
