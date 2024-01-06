from dotenv import load_dotenv

from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    API_KEY: str

    model_config = SettingsConfigDict(env_file=".env_app")


settings = Settings()
