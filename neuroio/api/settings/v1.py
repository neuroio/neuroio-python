from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync


class Settings(APIBase):
    def get(self) -> Response:
        try:
            return self.client.get(url="/v1/settings/thresholds/")
        finally:
            self.client.close()

    def update(
        self, exact: float = 79.3, ha: float = 75.5, junk: float = 68.84
    ) -> Response:
        data = locals()
        del data["self"]
        try:
            return self.client.patch(url="/v1/settings/thresholds/", data=data)
        finally:
            self.client.close()

    def reset(self) -> Response:
        try:
            return self.client.post(url="/v1/settings/thresholds/reset/")
        finally:
            self.client.close()


class SettingsAsync(APIBaseAsync):
    async def get(self) -> Response:
        try:
            return await self.client.get(url="/v1/settings/thresholds/")
        finally:
            await self.client.aclose()

    async def update(
        self, exact: float = 79.3, ha: float = 75.5, junk: float = 68.84
    ) -> Response:
        data = locals()
        del data["self"]
        try:
            return await self.client.patch(
                url="/v1/settings/thresholds/", data=data
            )
        finally:
            await self.client.aclose()

    async def reset(self) -> Response:
        try:
            return await self.client.post(url="/v1/settings/thresholds/reset/")
        finally:
            await self.client.aclose()
