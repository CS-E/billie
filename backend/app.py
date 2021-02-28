from fastapi import FastAPI

app = FastAPI()

from backend.models import SignupBody, LoginBody

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
