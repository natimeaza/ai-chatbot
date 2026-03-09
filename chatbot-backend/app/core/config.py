
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # App settings
    app_name: str = "AI Chatbot Backend"
    app_version: str = "0.1.0"
    debug: bool = True

    # Server settings
    host: str = "0.0.0.0"
    port: int = 8000

    # Database (for later)
    database_url: Optional[str] = None

    # LLM API keys (add to .env)
    openai_api_key: Optional[str] = None
    groq_api_key: Optional[str] = None

    # CORS origins
    cors_origins: list[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]

    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()


def get_settings() -> Settings:
    return settings


# Usage: from app.core.config import get_settings
# settings = get_settings()