from typing import BinaryIO

from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync


class Persons(APIBase):
    def create(
        self,
        image: BinaryIO,
        source: str,
        facesize: int,
        create_on_ha: bool,
        create_on_junk: bool,
        identify_asm: bool,
    ) -> Response:
        files = {"upload-file": image}
        data = {
            "source": source,
            "facesize": facesize,
            "create_on_ha": create_on_ha,
            "create_on_junk": create_on_junk,
            "identify_asm": identify_asm,
        }
        try:
            return self.client.post(url="/v1/persons/", files=files, json=data)
        finally:
            self.client.close()

    def create_by_entry(
        self, id: int, create_on_ha: bool, create_on_junk: bool
    ) -> Response:
        data = {
            "id": id,
            "create_on_ha": create_on_ha,
            "create_on_junk": create_on_junk,
        }
        try:
            return self.client.post(url="/v1/persons/entry/", json=data)
        finally:
            self.client.close()

    def delete(self, pid: str) -> Response:
        try:
            return self.client.delete(url=f"/v1/persons/{pid}/")
        finally:
            self.client.close()


class PersonsAsync(APIBaseAsync):
    async def create(
        self,
        image: BinaryIO,
        source: str,
        facesize: int,
        create_on_ha: bool,
        create_on_junk: bool,
        identify_asm: bool,
    ) -> Response:
        files = {"upload-file": image}
        data = {
            "source": source,
            "facesize": facesize,
            "create_on_ha": create_on_ha,
            "create_on_junk": create_on_junk,
            "identiry_asm": identify_asm,
        }
        try:
            return await self.client.post(
                url="/v1/persons/", files=files, json=data
            )
        finally:
            await self.client.aclose()

    async def create_by_entry(
        self, id: int, create_on_ha: bool, create_on_junk: bool
    ) -> Response:
        data = {
            "id": id,
            "create_on_ha": create_on_ha,
            "create_on_junk": create_on_junk,
        }
        try:
            return await self.client.post(url="/v1/persons/entry/", json=data)
        finally:
            await self.client.aclose()

    async def delete(self, pid: str) -> Response:
        try:
            return await self.client.delete(url=f"/v1/persons/{pid}/")
        finally:
            await self.client.aclose()
