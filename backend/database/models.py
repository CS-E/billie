from .database import Base


class User(Base):
    __tablename__ = "users"




class Tweets(Base):
    __tablename__ = "tweets"
