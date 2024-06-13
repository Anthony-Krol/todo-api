from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str = "your_secret_key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    database_url: str = "sqlite:///./test.db"

settings = Settings()
