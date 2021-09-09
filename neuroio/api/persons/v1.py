from typing import BinaryIO, Tuple, Union

from httpx import Response

from neuroio.api.base import APIBase, APIBaseAsync
from neuroio.constants import EntryResult, sentinel
from neuroio.utils import (
    prepare_image_processing,
    request_dict_processing,
    request_form_processing,
)


class Persons(APIBase):
    def create(
        self,
        image: Union[BinaryIO, Tuple[str, BinaryIO], bytes],
        source: str,
        facesize: Union[int, object] = sentinel,
        create_on_ha: Union[bool, object] = sentinel,
        create_on_junk: Union[bool, object] = sentinel,
        identify_asm: Union[bool, object] = sentinel,
    ) -> Response:
        data = request_form_processing(locals(), ["self", "image"])
        image = prepare_image_processing(image)
        files = {"image": image}

        with self.get_client() as client:
            return client.post(url="/v1/persons/", data=data, files=files)

    def create_by_entry(
        self, id: int, create_on_ha: bool, create_on_junk: bool
    ) -> Response:
        data = request_dict_processing(locals(), ["self"])

        with self.get_client() as client:
            return client.post(url="/v1/persons/entry/", json=data)

    def reinit(self, id: int) -> Response:
        with self.get_client() as client:
            return client.post(url="/v1/persons/reinit/", json={"id": id})

    def reinit_by_photo(
        self,
        pid: str,
        image: Union[BinaryIO, Tuple[str, BinaryIO], bytes],
        source: str,
        facesize: Union[int, object] = sentinel,
        identify_asm: Union[bool, object] = sentinel,
        result: str = EntryResult.HA,
    ) -> Response:
        data = request_form_processing(locals())
        image = prepare_image_processing(image)
        files = {"image": image}

        with self.get_client() as client:
            return client.post(
                url=f"/v1/persons/reinit/{pid}/", data=data, files=files
            )

    def search(
        self,
        image: Union[BinaryIO, Tuple[str, BinaryIO], bytes],
        identify_asm: bool = False,
    ) -> Response:
        if isinstance(image, tuple):
            image = image[1]
        files = {"image": ("image", image, "image/jpeg")}
        data = {"identify_asm": str(identify_asm)}

        with self.get_client() as client:
            return client.post(
                url="/v1/persons/search/", data=data, files=files
            )

    def delete(self, pid: str) -> Response:
        with self.get_client() as client:
            return client.delete(url=f"/v1/persons/{pid}/")


class PersonsAsync(APIBaseAsync):
    async def create(
        self,
        image: Union[BinaryIO, Tuple[str, BinaryIO], bytes],
        source: str,
        facesize: Union[int, object] = sentinel,
        create_on_ha: Union[bool, object] = sentinel,
        create_on_junk: Union[bool, object] = sentinel,
        identify_asm: Union[bool, object] = sentinel,
    ) -> Response:
        data = request_form_processing(locals(), ["self", "image"])
        image = prepare_image_processing(image)
        files = {"image": image}

        async with self.get_client() as client:
            return await client.post(
                url="/v1/persons/", data=data, files=files
            )

    async def create_by_entry(
        self, id: int, create_on_ha: bool, create_on_junk: bool
    ) -> Response:
        data = request_dict_processing(locals(), ["self"])

        async with self.get_client() as client:
            return await client.post(url="/v1/persons/entry/", json=data)

    async def reinit(self, id: int) -> Response:
        async with self.get_client() as client:
            return await client.post(
                url="/v1/persons/reinit/", json={"id": id}
            )

    async def reinit_by_photo(
        self,
        pid: str,
        image: Union[BinaryIO, Tuple[str, BinaryIO], bytes],
        source: str,
        facesize: Union[int, object] = sentinel,
        identify_asm: Union[bool, object] = sentinel,
        result: str = EntryResult.HA,
    ) -> Response:
        data = request_form_processing(locals(), ["self", "image", "pid"])
        image = prepare_image_processing(image)
        files = {"image": image}

        async with self.get_client() as client:
            return await client.post(
                url=f"/v1/persons/reinit/{pid}/", data=data, files=files
            )

    async def search(
        self,
        image: Union[BinaryIO, Tuple[str, BinaryIO], bytes],
        identify_asm: bool = False,
    ) -> Response:
        if isinstance(image, tuple):
            image = image[1]

        files = {"image": ("image", image, "image/jpeg")}
        data = {"identify_asm": str(identify_asm)}

        async with self.get_client() as client:
            return await client.post(
                url="/v1/persons/search/", data=data, files=files
            )

    async def delete(self, pid: str) -> Response:
        async with self.get_client() as client:
            return await client.delete(url=f"/v1/persons/{pid}/")
