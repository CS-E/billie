from pydantic import BaseModel

class Settings(BaseSettings):
    twitter_secret: str

    class Config:
        env_file = ".env"
