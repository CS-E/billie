from pydantic import BaseModel

class SignupBody(BaseModel):
    user_email: str
    user_password: str
    user_twitter_handle: str
    full_name: Optional[str] = None

class LoginBody(BaseModel):
    user_password: str
    user_twitter_handle: str