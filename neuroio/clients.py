import enum
from typing import Any, Dict, Optional

from neuroio import constants
from neuroio.auth_token import AuthorizationTokenAuth
from neuroio.base import APIBase
from neuroio.utils import cached_property, dynamic_import, get_package_version


class Service(str, enum.Enum):
    API = "api"
    IAM = "iam"


class Client:
    def __init__(
        self,
        api_token: Optional[str] = None,
        api_version: int = 1,
        timeout: float = constants.HTTP_CLIENT_TIMEOUT,
    ):
        """
        Creates and manages singleton of HTTP client, that is used to make
        request to API.
        """
        self.api_token = api_token
        self.api_version = api_version

        self.csettings = self.client_settings(timeout=timeout)
        self.init()

    def init(self) -> None:
        self.api_atrr_names = [
            "sources",
            "entries",
            "streams",
            "utility",
            "settings",
            "groups",
            "persons",
            "notifications",
        ]
        self.iam_atrr_names = [
            "auth",
            "spaces",
            "lists",
            "licenses",
            "whoami",
            "tokens",
            "billing",
        ]

    @cached_property
    def is_async(self) -> bool:
        return self.__class__.__name__ == "AsyncClient"

    @property
    def common_headers(self) -> dict:
        root = "neuroio-python"
        if self.is_async:
            root = "neuroio-async-python"
        return {"User-Agent": f"{root}/{get_package_version()}"}

    def client_settings(self, timeout: float) -> Dict[Any, Any]:
        settings = {
            "timeout": timeout,
            "headers": self.common_headers,
        }
        if self.api_token:
            settings["auth"] = AuthorizationTokenAuth(api_token=self.api_token)

        return settings

    def get_api_class_instance(
        self, namespace: str, clsname: str, service: Service = Service.API
    ) -> APIBase:
        abs_path = f"neuroio.{namespace}.v{self.api_version}"
        cls = dynamic_import(abs_path=abs_path, attribute=clsname)
        return cls(settings=self.csettings)

    def get_attr_instance_by_name(
        self,
        attr_name: str,
        is_async: bool = False,
        service: Service = Service.API,
    ) -> APIBase:
        return self.get_api_class_instance(
            namespace=attr_name,
            clsname=attr_name.capitalize() + ("Async" if is_async else ""),
            service=service,
        )

    class Lists:
        def __init__(self, parent: Any) -> None:
            self.parent = parent

        @cached_property
        def spaces(self) -> APIBase:
            return self.parent.get_api_class_instance(
                namespace="lists.spaces",
                clsname=(
                    "ListsSpaces" + ("Async" if self.parent.is_async else "")
                ),
                service=Service.IAM,
            )

    class Licenses:
        def __init__(self, parent: Any) -> None:
            self.parent = parent

        @cached_property
        def sources(self) -> APIBase:
            return self.parent.get_api_class_instance(
                namespace="licenses.sources",
                clsname=(
                    "Licenses" + ("Async" if self.parent.is_async else "")
                ),
                service=Service.IAM,
            )

    class Streams:
        def __init__(self, parent: Any) -> None:
            self.parent = parent

        @cached_property
        def tokens(self) -> APIBase:
            return self.parent.get_api_class_instance(
                namespace="streams.tokens",
                clsname="StreamTokens"
                + ("Async" if self.parent.is_async else ""),
            )

    def __getattr__(self, name: str) -> Any:
        if name in self.iam_atrr_names:
            if name == "lists":
                return Client.Lists(self)
            elif name == "licenses":
                return Client.Licenses(self)
            else:
                return self.get_attr_instance_by_name(
                    attr_name=name,
                    is_async=self.is_async,
                    service=Service.IAM,
                )
        elif name in self.api_atrr_names:
            if name == "streams":
                return Client.Streams(self)
            else:
                return self.get_attr_instance_by_name(
                    attr_name=name, is_async=self.is_async
                )
        else:
            # Default behaviour
            raise AttributeError


class AsyncClient(Client):
    pass
