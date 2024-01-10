from dotenv import load_dotenv

from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class SettingsMinio(BaseSettings):
    ACCESS_KEY: str
    SECRET_KEY: str

settings_minio = SettingsMinio()
