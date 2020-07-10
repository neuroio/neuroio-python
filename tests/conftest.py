import pytest

from neuroio import AsyncClient, Client


@pytest.fixture
def client():
    return Client()


@pytest.fixture
async def async_client():
    return AsyncClient()
