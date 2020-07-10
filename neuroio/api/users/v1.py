from typing import Union

from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync


class Users(APIBase):
    def tokens(self, permanent: bool = None) -> Response:
        data = {"permanent": permanent} if permanent is not None else None
        try:
            return self.client.get(url="/v1/users/tokens/", params=data)
        finally:
            self.client.close()

    def token_info(self, token_id_or_key: Union[int, str]) -> Response:
        try:
            return self.client.get(url=f"/v1/users/tokens/{token_id_or_key}/")
        finally:
            self.client.close()


class UsersAsync(APIBaseAsync):
    async def tokens(self, permanent: bool = None) -> Response:
        data = {"permanent": permanent} if permanent is not None else None
        try:
            return await self.client.get(url="/v1/users/tokens/", params=data)
        finally:
            await self.client.aclose()

    async def token_info(self, token_id_or_key: Union[int, str]) -> Response:
        try:
            return await self.client.get(
                url=f"/v1/users/tokens/{token_id_or_key}/"
            )
        finally:
            await self.client.aclose()
