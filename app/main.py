from fastapi import Body, FastAPI, Request
from pydantic import HttpUrl

from app.config import settings
from app import models

from lib.telegram import Telegram
from lib import schema

from devtools import debug

app = FastAPI()
telegram = Telegram(settings.TELEGRAM_BOT_TOKEN)

# fastapi가 처음 실행 됬을때
@app.on_event("startup")
def on_startup():
    from app.database import engine

    models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def hello():
    return b"hello World!"

@app.post("/")
async def webhook(request: Request):
    r = await request.json()
    debug(r)
    r = schema.Update.parse_obj(r)
    return "OK"

@app.get("/me")
async def get_me():
    return await telegram.get_bot_info()

@app.get("/wb")
async def get_webhook():
    return await telegram.get_webhook()

@app.post("/wb")
async def set_webhook(url: HttpUrl = Body(..., embed=True)):
    return await telegram.set_webhook(url)