import httpx
from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync


class Whoami(APIBase):
    def me(self) -> Response:
        with httpx.Client(**self.settings) as client:
            return client.get(url="/v1/whoami/")


class WhoamiAsync(APIBaseAsync):
    async def me(self) -> Response:
        async with httpx.AsyncClient(**self.settings) as client:
            return await client.get(url="/v1/whoami/")
