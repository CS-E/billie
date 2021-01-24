from typing import List, Optional
from pydantic import BaseModel


class TweetBase(BaseModel):
    title: str
    description: Optional[str] = None


class Item(TweetBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    twitter_handle: str

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True