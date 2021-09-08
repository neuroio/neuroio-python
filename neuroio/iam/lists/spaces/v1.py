from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync


class ListsSpaces(APIBase):
    def all(self) -> Response:
        with self.get_client() as client:
            return client.get(url="/v1/lists/spaces/")


class ListsSpacesAsync(APIBaseAsync):
    async def all(self) -> Response:
        async with self.get_client() as client:
            return await client.get(url="/v1/lists/spaces/")
