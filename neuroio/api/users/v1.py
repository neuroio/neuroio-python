from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync


class Users(APIBase):
    def tokens(self, permanent: bool = None) -> Response:
        data = {"permanent": permanent} if permanent is not None else None
        try:
            return self.client.get(url="/v1/users/tokens/", params=data)
        finally:
            self.client.close()


class UsersAsync(APIBaseAsync):
    async def tokens(self, permanent: bool = None) -> Response:
        data = {"permanent": permanent} if permanent is not None else None
        try:
            return await self.client.get(url="/v1/users/tokens/", params=data)
        finally:
            await self.client.aclose()
