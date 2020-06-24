from functools import cached_property
from typing import Optional, Type, Union

import httpx

from neuroio import constants
from neuroio.api.base import APIBase
from neuroio.auth import AuthorizationTokenAuth
from neuroio.utils import dynamic_import, get_package_version


class Client:
    def __init__(
        self,
        api_token: Optional[str] = None,
        api_version: int = 1,
        timeout: Optional[float] = None,
    ):
        """
        Creates and manages singleton of HTTP client, that is used to make
        request to API.
        """
        self.api_token = api_token
        self.api_version = api_version
        self.client = self.httpx_client_class(
            base_url=constants.API_BASE_URL,
            headers=self.common_headers,
            timeout=timeout or constants.HTTP_CLIENT_TIMEOUT,
        )
        self.inject_api_token()

    @property
    def httpx_client_class(
        self
    ) -> Union[Type[httpx.Client], Type[httpx.AsyncClient]]:
        return httpx.Client

    @property
    def common_headers(self) -> dict:
        return {"User-Agent": f"neuroio-python/{get_package_version()}"}

    def inject_api_token(self, api_token: Optional[str] = None) -> None:
        # Override api token only if provided api_token is not empty or None
        if api_token:
            self.api_token = api_token

        # Injecting auth only if api_token is not empty or None
        if self.api_token:
            self.client.auth = AuthorizationTokenAuth(api_token=self.api_token)

    def get_api_class_instance(self, namespace: str, clsname: str) -> APIBase:
        abs_path = f"{namespace}.v{self.api_version}"
        cls = dynamic_import(abs_path=abs_path, attribute=clsname)
        return cls(client=self.client)

    @cached_property
    def auth(self) -> APIBase:
        return self.get_api_class_instance(
            namespace="neuroio.api.auth", clsname="Auth"
        )


class AsyncClient(Client):
    @property
    def httpx_client_class(
        self
    ) -> Union[Type[httpx.Client], Type[httpx.AsyncClient]]:
        return httpx.AsyncClient

    @property
    def common_headers(self) -> dict:
        return {"User-Agent": f"neuroio-async-python/{get_package_version()}"}

    @cached_property
    def auth(self) -> APIBase:
        return self.get_api_class_instance(
            namespace="neuroio.api.auth", clsname="AuthAsync"
        )
