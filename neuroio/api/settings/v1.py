import httpx
from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync
from neuroio.constants import (
    DEFAULT_EXACT_THRESHOLD,
    DEFAULT_HA_THRESHOLD,
    DEFAULT_JUNK_THRESHOLD,
)
from neuroio.utils import request_dict_processing


class Settings(APIBase):
    def get(self) -> Response:
        with httpx.Client(**self.settings) as client:
            return client.get(url="/v1/settings/thresholds/")

    def update(
        self,
        exact: float = DEFAULT_EXACT_THRESHOLD,
        ha: float = DEFAULT_HA_THRESHOLD,
        junk: float = DEFAULT_JUNK_THRESHOLD,
    ) -> Response:
        data = request_dict_processing(locals(), ["self"])

        with httpx.Client(**self.settings) as client:
            return client.patch(url="/v1/settings/thresholds/", data=data)

    def reset(self) -> Response:
        with httpx.Client(**self.settings) as client:
            return client.post(url="/v1/settings/thresholds/reset/")


class SettingsAsync(APIBaseAsync):
    async def get(self) -> Response:
        async with httpx.AsyncClient(**self.settings) as client:
            return await client.get(url="/v1/settings/thresholds/")

    async def update(
        self,
        exact: float = DEFAULT_EXACT_THRESHOLD,
        ha: float = DEFAULT_HA_THRESHOLD,
        junk: float = DEFAULT_JUNK_THRESHOLD,
    ) -> Response:
        data = request_dict_processing(locals(), ["self"])

        async with httpx.AsyncClient(**self.settings) as client:
            return await client.patch(
                url="/v1/settings/thresholds/", data=data
            )

    async def reset(self) -> Response:
        async with httpx.AsyncClient(**self.settings) as client:
            return await client.post(url="/v1/settings/thresholds/reset/")
