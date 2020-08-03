from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync


class Spaces(APIBase):
    def create(self, name: str) -> Response:
        data = {"name": name}
        try:
            return self.client.post(url="/v1/spaces/", json=data)
        finally:
            self.client.close()


class SpacesAsync(APIBaseAsync):
    async def create(self, name: str) -> Response:
        data = {"name": name}
        try:
            return await self.client.post(url="/v1/spaces/", json=data)
        finally:
            await self.client.aclose()
