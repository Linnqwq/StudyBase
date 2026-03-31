from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    supabase_url: str
    supabase_secret_key: str
    database_url: str
    storage_bucket: str

    class Config:
        env_file = ".env"

settings = Settings()