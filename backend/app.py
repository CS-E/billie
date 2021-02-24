import base64
import hashlib
import hmac
import os

from typing import Optional


from fastapi import FastAPI

app = FastAPI()

from backend.models import SignupBody, LoginBody
from backend.config import Settings

settings = Settings()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/signup", status_code=201)
async def signup(signup_body: SignupBody):
    pass

@app.post("/login", status_code=200)
async def login(login_body: LoginBody):
    pass


@app.get("/{user_id}/all_tweets", status_code=200)
async def get_tweets(user_id: int):
    return {"id": user_id}


@app.get("/webhook/crc", status_code=200)
async def get_crc_response(crc_token: str):
    # creates HMAC SHA-256 hash from incomming token and your consumer secret
    # and constructs response data with base64 encoded hash
    sha256_hash_digest = hmac.new(settings.twitter_secret, msg=crc_token, digestmod=hashlib.sha256).digest()
    response = {
        'response_token': 'sha256=' + base64.b64encode(sha256_hash_digest)
    }
    return response
