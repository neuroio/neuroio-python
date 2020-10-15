from typing import List, Union

from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync
from neuroio.constants import (
    EntryLiveness,
    EntryMood,
    EntryResult,
    HttpMethod,
    Sex,
    sentinel,
)
from neuroio.utils import request_dict_processing, request_query_processing


class Notifications(APIBase):
    def create(
        self,
        name: str,
        http_method: HttpMethod,
        destination_url: str,
        is_active: bool = True,
        moods: Union[List[EntryMood], object] = sentinel,
        results: Union[List[EntryResult], object] = sentinel,
        liveness: Union[List[EntryLiveness], object] = sentinel,
        age_from: Union[int, object] = sentinel,
        age_to: Union[int, object] = sentinel,
        sex: Union[List[Sex], object] = sentinel,
        sources: Union[List[int], object] = sentinel,
        persons_groups: Union[List[int], object] = sentinel,
    ) -> Response:
        data = request_dict_processing(locals(), ["self"])

        return self.client.post(url="/v1/notifications/", json=data)

    def list(
        self,
        q: Union[str, object] = sentinel,
        spaces_ids: Union[List[int], object] = sentinel,
        limit: int = 20,
        offset: int = 0,
    ) -> Response:
        data = request_query_processing(locals(), ["self"])

        return self.client.get(url="/v1/notifications/", params=data)

    def get(self, id: int) -> Response:
        return self.client.get(url=f"/v1/notifications/{id}/")

    def update(
        self,
        id: int,
        name: str,
        http_method: HttpMethod,
        destination_url: str,
        is_active: bool = True,
        moods: Union[List[EntryMood], object] = sentinel,
        results: Union[List[EntryResult], object] = sentinel,
        liveness: Union[List[EntryLiveness], object] = sentinel,
        age_from: Union[int, object] = sentinel,
        age_to: Union[int, object] = sentinel,
        sex: Union[List[Sex], object] = sentinel,
        sources: Union[List[int], object] = sentinel,
        persons_groups: Union[List[int], object] = sentinel,
    ) -> Response:
        data = request_dict_processing(locals(), ["self", "id"])

        return self.client.patch(url=f"/v1/notifications/{id}/", json=data)

    def delete(self, id: int) -> Response:
        return self.client.delete(url=f"/v1/notifications/{id}/")


class NotificationsAsync(APIBaseAsync):
    async def create(
        self,
        name: str,
        http_method: HttpMethod,
        destination_url: str,
        is_active: bool = True,
        moods: Union[List[EntryMood], object] = sentinel,
        results: Union[List[EntryResult], object] = sentinel,
        liveness: Union[List[EntryLiveness], object] = sentinel,
        age_from: Union[int, object] = sentinel,
        age_to: Union[int, object] = sentinel,
        sex: Union[List[Sex], object] = sentinel,
        sources: Union[List[int], object] = sentinel,
        persons_groups: Union[List[int], object] = sentinel,
    ) -> Response:
        data = request_dict_processing(locals(), ["self"])

        return await self.client.post(url="/v1/notifications/", json=data)

    async def list(
        self,
        q: Union[str, object] = sentinel,
        spaces_ids: Union[List[int], object] = sentinel,
        limit: int = 20,
        offset: int = 0,
    ) -> Response:
        data = request_query_processing(locals(), ["self"])

        return await self.client.get(url="/v1/notifications/", params=data)

    async def get(self, id: int) -> Response:
        return await self.client.get(url=f"/v1/notifications/{id}/")

    async def update(
        self,
        id: int,
        name: str,
        http_method: HttpMethod,
        destination_url: str,
        is_active: bool = True,
        moods: Union[List[EntryMood], object] = sentinel,
        results: Union[List[EntryResult], object] = sentinel,
        liveness: Union[List[EntryLiveness], object] = sentinel,
        age_from: Union[int, object] = sentinel,
        age_to: Union[int, object] = sentinel,
        sex: Union[List[Sex], object] = sentinel,
        sources: Union[List[int], object] = sentinel,
        persons_groups: Union[List[int], object] = sentinel,
    ) -> Response:
        data = request_dict_processing(locals(), ["self", "id"])
        return await self.client.patch(
            url=f"/v1/notifications/{id}/", json=data
        )

    async def delete(self, id: int) -> Response:
        return await self.client.delete(url=f"/v1/notifications/{id}/")
