import functools
from importlib import import_module
from typing import Any, Callable, TypeVar


def get_package_version() -> str:
    from neuroio import __version__

    return __version__


def dynamic_import(abs_path: str, attribute: str) -> Any:
    """
    Imports any attribute from the module specified as string dotted path.
    Takes into account current supplied version to the Client instance.

    :param abs_path: dotted path of the module from which to import from
    :param attribute: function, class or any other attr to be imported
    :return: imported attribute
    """
    module_object = import_module(abs_path)
    return getattr(module_object, attribute)


F = TypeVar("F", bound=Callable[..., Any])


def cached_property(f: F) -> property:
    return property(functools.lru_cache()(f))


def process_query_params(params: dict) -> dict:
    for key, item in params.items():
        if isinstance(item, list):
            params[key] = ",".join(map(str, item))
    return params
