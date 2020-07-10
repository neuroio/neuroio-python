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

    def token_update(
        self, token_id_or_key: Union[int, str], is_active: bool
    ) -> Response:
        try:
            return self.client.patch(
                url=f"/v1/users/tokens/{token_id_or_key}/",
                data={"is_active": is_active},
            )
        finally:
            self.client.close()

    def tokens_delete(self) -> Response:
        try:
            return self.client.delete(url="/v1/users/tokens/")
        finally:
            self.client.close()

    def token_delete(self, token_id_or_key: Union[int, str]) -> Response:
        try:
            return self.client.delete(
                url=f"/v1/users/tokens/{token_id_or_key}/"
            )
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

    async def token_update(
        self, token_id_or_key: Union[int, str], is_active: bool
    ) -> Response:
        try:
            return await self.client.patch(
                url=f"/v1/users/tokens/{token_id_or_key}/",
                data={"is_active": is_active},
            )
        finally:
            await self.client.aclose()

    async def tokens_delete(self) -> Response:
        try:
            return await self.client.delete(url="/v1/users/tokens/")
        finally:
            await self.client.aclose()

    async def token_delete(self, token_id_or_key: Union[int, str]) -> Response:
        try:
            return await self.client.delete(
                url=f"/v1/users/tokens/{token_id_or_key}/"
            )
        finally:
            await self.client.aclose()
