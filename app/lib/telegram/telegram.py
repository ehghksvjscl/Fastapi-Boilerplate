from ctypes import Union
from http import client
from typing import Union

import httpx # requests는 비동기를 지원하지 않음
from  pydantic import SecretStr

class Telegram:
    API_HOST = 'https://api.telegram.org'

    def __init__(self, token: Union[str, SecretStr]) -> None:
        self._token = token
        self.client = httpx.AsyncClient(base_url=self.host) # 비동기

    @property
    def token(self):
        if isinstance(self._token, SecretStr):
            return self._token.get_secret_value() # SecretStr mode
        
        return self._token # str mode

    @property
    def host(self):
        return f"{self.API_HOST}/bot{self.token}"

    async def get_bot_info(self) -> dict:
        r = await self.client.get("getMe")
        return r.json()

    async def get_webhook(self) -> dict:
        r = await self.client.get("getWebhookInfo")
        return r.json()

    async def set_webhook(self, url) -> dict:
        r = await self.client.post("setWebhook", data={"url": url})
        return r.json()

    async def send_message(self, chat_id: int, text: str):
        r = await self.client.post("sendMessage", data={
            "chat_id":chat_id,
            "text": text
        })
        return r.json()