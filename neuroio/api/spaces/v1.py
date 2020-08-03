from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync


class Spaces(APIBase):
    def create(self, name: str) -> Response:
        data = {"name": name}
        try:
            return self.client.post(url="/v1/spaces/", json=data)
        finally:
            self.client.close()

    def list(
        self, q: str = None, limit: int = 20, offset: int = 0
    ) -> Response:
        data = {"q": q, "limit": limit, "offset": offset}
        try:
            return self.client.get(url="/v1/spaces/", params=data)
        finally:
            self.client.close()

    def get(self, id: int) -> Response:
        try:
            return self.client.get(url=f"/v1/spaces/{id}/")
        finally:
            self.client.close()


class SpacesAsync(APIBaseAsync):
    async def create(self, name: str) -> Response:
        data = {"name": name}
        try:
            return await self.client.post(url="/v1/spaces/", json=data)
        finally:
            await self.client.aclose()

    async def list(
        self, q: str = None, limit: int = 20, offset: int = 0
    ) -> Response:
        data = {"q": q, "limit": limit, "offset": offset}
        try:
            return await self.client.get(url="/v1/spaces/", params=data)
        finally:
            await self.client.aclose()

    async def get(self, id: int) -> Response:
        try:
            return await self.client.get(url=f"/v1/spaces/{id}/")
        finally:
            await self.client.aclose()
