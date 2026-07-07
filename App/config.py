from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os
load_dotenv()

class Settings(BaseSettings):
    SUPABASE_URL: str
    SUPABASE_KEY: str
    secret_key: str
    algo: str
    expireTime: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"), os.getenv("SECRET_KEY"), os.getenv("ALGORITHM"), os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))