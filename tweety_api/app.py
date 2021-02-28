import base64
import hashlib
import hmac
import os
import codecs
import json

from fastapi import FastAPI
from config import Settings

app = FastAPI()
settings = Settings()

@app.get("/webhooks/twitter", status_code=200)
async def get_crc_response(crc_token: str):
    # creates HMAC SHA-256 hash from incomming token and your consumer secret
    # and constructs response data with base64 encoded hash
    sha256_hash_digest = hmac.new(settings.twitter_secret.encode('utf-8'), msg=crc_token.encode('utf-8'), digestmod=hashlib.sha256).digest()
    response = {
        'response_token': 'sha256=' + base64.b64encode(sha256_hash_digest).decode('utf-8')
    }
    return response


@app.post("/webhooks/twitter", status_code=200)
async def get_webhook_data():
    # TODO: Setup collection of data from webhook
    return "response"