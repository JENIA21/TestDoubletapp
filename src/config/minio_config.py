from dotenv import load_dotenv

from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class SettingsMinio(BaseSettings):
    ACCESSKEY: str
    SECRETKEY: str

    model_config = SettingsConfigDict(env_file=".env.minio")


settings = SettingsMinio()