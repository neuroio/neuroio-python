import pytest

from neuroio import AsyncClient, Client


@pytest.fixture
def client_no_auth():
    return Client()


@pytest.fixture
async def async_client_no_auth():
    return AsyncClient()


@pytest.fixture
def client():
    return Client(api_token="token")


@pytest.fixture
async def async_client():
    return AsyncClient(api_token="token")
