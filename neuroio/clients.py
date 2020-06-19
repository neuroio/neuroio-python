from typing import Type, Union

import httpx

from neuroio import constants
from neuroio.auth import AuthorizationTokenAuth
from neuroio.utils import get_package_version


class Client:
    def __init__(
        self, api_token: str, api_version: int = 1, timeout: float = None
    ):
        """
        Creates and manages singleton of HTTP client, that is used to make
        request to API.

        Since the only unauthorized API endpoint is version, let's require
        API token for any instantiation of the Client class.
        """
        self.api_version = api_version
        self.client = self.httpx_client_class(
            auth=AuthorizationTokenAuth(api_token=api_token),
            base_url=constants.API_BASE_URL,
            headers=self.common_headers,
            timeout=timeout or constants.HTTP_CLIENT_TIMEOUT,
        )

    @property
    def httpx_client_class(
        self
    ) -> Union[Type[httpx.Client], Type[httpx.AsyncClient]]:
        return httpx.Client

    @property
    def common_headers(self) -> dict:
        return {"User-Agent": f"neuroio-python/{get_package_version()}"}


class AsyncClient(Client):
    @property
    def httpx_client_class(
        self
    ) -> Union[Type[httpx.Client], Type[httpx.AsyncClient]]:
        return httpx.AsyncClient

    @property
    def common_headers(self) -> dict:
        return {"User-Agent": f"neuroio-async-python/{get_package_version()}"}
