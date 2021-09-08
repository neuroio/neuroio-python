from datetime import datetime
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


class Licenses(APIBase):
    def create(self, name: str, entry_storage_days: int = 1) -> Response:
        data = request_dict_processing(locals(), ["self"])

        with self.get_client() as client:
            return client.post(url="/v1/licenses/sources", json=data)

    def list(
        self,
        q: str,
        date_from: Union[datetime, object] = sentinel,
        date_to: Union[datetime, object] = sentinel,
        limit: int = 20,
        offset: int = 0,
    ) -> Response:
        data = request_query_processing(locals(), ["self"])

        with self.get_client() as client:
            return client.get(url="/v1/licenses/sources/", params=data)

    def get(self, id: int) -> Response:
        with self.get_client() as client:
            return client.get(url=f"/v1/licenses/sources/{id}/")

    def update(
        self,
        id: int,
        name: str,
        is_active: bool = True,
        entry_storage_days: int = 1,
    ) -> Response:
        data = request_dict_processing(locals(), ["self", "id"])

        with self.get_client() as client:
            return client.patch(url=f"/v1/licenses/sources/{id}/", json=data)


class LicensesAsync(APIBaseAsync):
    async def create(self, name: str, entry_storage_days: int = 1) -> Response:
        data = request_dict_processing(locals(), ["self"])

        async with self.get_client() as client:
            return await client.post(url="/v1/licenses/sources/", json=data)

    async def list(
        self,
        q: Union[str, object] = sentinel,
        spaces_ids: Union[List[int], object] = sentinel,
        limit: int = 20,
        offset: int = 0,
    ) -> Response:
        data = request_query_processing(locals(), ["self"])

        async with self.get_client() as client:
            return await client.get(url="/v1/licenses/sources/", params=data)

    async def get(self, id: int) -> Response:
        async with self.get_client() as client:
            return await client.get(url=f"/v1/licenses/sources/{id}/")

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
        async with self.get_client() as client:
            return await client.patch(
                url=f"/v1/licenses/sources/{id}/", json=data
            )

