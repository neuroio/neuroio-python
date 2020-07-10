import pytest
import respx

from neuroio.constants import API_BASE_URL


@respx.mock
def test_tokens_list_200(client):
    request = respx.get(
        f"{API_BASE_URL}/v1/users/tokens/",
        status_code=200,
        content=[{"token": "key"}, {"token": "key2"}],
    )
    tokens = client.users.tokens()
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()[0]["token"] == "key"
    assert tokens.json()[1]["token"] == "key2"


@respx.mock
def test_tokens_permanent_list_200(client):
    request = respx.get(
        f"{API_BASE_URL}/v1/users/tokens/?permanent=true",
        status_code=200,
        content=[{"token": "key"}],
    )
    tokens = client.users.tokens(permanent=True)
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()[0]["token"] == "key"


@respx.mock
def test_tokens_not_permanent_list_200(client):
    request = respx.get(
        f"{API_BASE_URL}/v1/users/tokens/?permanent=false",
        status_code=200,
        content=[{"token": "key"}],
    )
    tokens = client.users.tokens(permanent=False)
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()[0]["token"] == "key"


@respx.mock
@pytest.mark.asyncio
async def test_async_tokens_list_200(async_client):
    request = respx.get(
        f"{API_BASE_URL}/v1/users/tokens/",
        status_code=200,
        content=[{"token": "key"}, {"token": "key2"}],
    )
    tokens = await async_client.users.tokens()
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()[0]["token"] == "key"


@respx.mock
@pytest.mark.asyncio
async def test_async_tokens_permanent_list_200(async_client):
    request = respx.get(
        f"{API_BASE_URL}/v1/users/tokens/?permanent=true",
        status_code=200,
        content=[{"token": "key"}],
    )
    tokens = await async_client.users.tokens(permanent=True)
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()[0]["token"] == "key"


@respx.mock
@pytest.mark.asyncio
async def test_async_tokens_not_permanent_list_200(async_client):
    request = respx.get(
        f"{API_BASE_URL}/v1/users/tokens/?permanent=false",
        status_code=200,
        content=[{"token": "key"}],
    )
    tokens = await async_client.users.tokens(permanent=False)
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()[0]["token"] == "key"
