from pydantic import BaseSettings

class Settings(BaseSettings):
    twitter_secret: str

    class Config:
        env_file = ".env"
