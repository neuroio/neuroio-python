import pytest

from neuroio import AsyncClient, Client


def test_client_instance():
    neuroio = Client(api_token="helloworld", api_version=2)
    assert neuroio.api_version == 2


def test_not_able_to_instantiate_client_without_api_key():
    with pytest.raises(Exception):
        Client(api_token="")


def test_async_client_different_user_agent_from_sync_client():
    neuroio = Client(api_token="helloworld")
    neuroio_async = AsyncClient(api_token="helloworld")
    assert (
        neuroio.client.headers["User-Agent"]
        != neuroio_async.client.headers["User-Agent"]
    )
