from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync


class Auth(APIBase):
    def login(self, username: str, password: str) -> Response:
        data = {"username": username, "password": password}
        try:
            return self.client.post(url="/v1/login/", data=data)
        finally:
            self.client.close()


class AuthAsync(APIBaseAsync):
    async def login(self, username: str, password: str) -> Response:
        data = {"username": username, "password": password}
        try:
            return await self.client.post(url="/v1/login/", data=data)
        finally:
            await self.client.aclose()
