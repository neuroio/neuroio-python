import pytest
import respx

from neuroio.constants import API_BASE_URL
from tests.utils import mock_query_params_all_combos


@respx.mock
def test_create_ok(client):
    request = respx.post(f"{API_BASE_URL}/v1/streams/tokens/").respond(
        status_code=201,
        json={"is_active": True},
    )
    response = client.streams.tokens.create()

    assert request.called
    assert response.status_code == 201
    assert response.json()["is_active"] is True


@respx.mock
def test_create_failed(client):
    request = respx.post(f"{API_BASE_URL}/v1/streams/tokens/").respond(
        status_code=400
    )
    response = client.streams.tokens.create(permanent=True)

    assert request.called
    assert response.status_code == 400


@respx.mock
@pytest.mark.asyncio
async def test_async_create_ok(async_client):
    request = respx.post(f"{API_BASE_URL}/v1/streams/tokens/").respond(
        status_code=201,
        json={"is_active": True},
    )
    response = await async_client.streams.tokens.create(permanent=True)

    assert request.called
    assert response.status_code == 201
    assert response.json()["is_active"] is True


@respx.mock
@pytest.mark.asyncio
async def test_async_create_failed(async_client):
    request = respx.post(f"{API_BASE_URL}/v1/streams/tokens/").respond(
        status_code=400
    )
    response = await async_client.streams.tokens.create(permanent=True)

    assert request.called
    assert response.status_code == 400


@respx.mock
def test_list_200(client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/streams/tokens",
        "permanent=true",
        "limit=20",
        "offset=0",
        json=[{"token": "key"}, {"token": "key2"}],
    )

    tokens = client.streams.tokens.list(permanent=True)
    assert any([request.called for request in requests])
    assert tokens.status_code == 200
    assert tokens.json()[0]["token"] == "key"
    assert tokens.json()[1]["token"] == "key2"


@respx.mock
def test_permanent_list_200(client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/streams/tokens",
        "permanent=true",
        "limit=20",
        "offset=0",
        json=[{"token": "key"}],
    )
    tokens = client.streams.tokens.list(permanent=True)

    assert any([request.called for request in requests])
    assert tokens.status_code == 200
    assert tokens.json()[0]["token"] == "key"


@respx.mock
def test_not_permanent_list_200(client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/streams/tokens",
        "permanent=false",
        "limit=20",
        "offset=0",
        json=[{"token": "key"}],
    )
    tokens = client.streams.tokens.list(permanent=False)
    assert any([request.called for request in requests])
    assert tokens.status_code == 200
    assert tokens.json()[0]["token"] == "key"


@respx.mock
@pytest.mark.asyncio
async def test_async_list_200(async_client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/streams/tokens",
        "permanent=",
        "limit=20",
        "offset=0",
        json=[{"token": "key"}, {"token": "key2"}],
    )
    tokens = await async_client.streams.tokens.list()

    assert any([request.called for request in requests])
    assert tokens.status_code == 200
    assert tokens.json()[0]["token"] == "key"


@respx.mock
@pytest.mark.asyncio
async def test_async_permanent_list_200(async_client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/streams/tokens",
        "permanent=true",
        "limit=20",
        "offset=0",
        json=[{"token": "key"}],
    )
    tokens = await async_client.streams.tokens.list(permanent=True)

    assert any([request.called for request in requests])
    assert tokens.status_code == 200
    assert tokens.json()[0]["token"] == "key"


@respx.mock
@pytest.mark.asyncio
async def test_async_not_permanent_list_200(async_client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/streams/tokens",
        "permanent=false",
        "limit=20",
        "offset=0",
        json=[{"token": "key"}],
    )
    tokens = await async_client.streams.tokens.list(permanent=False)

    assert any([request.called for request in requests])
    assert tokens.status_code == 200
    assert tokens.json()[0]["token"] == "key"


@respx.mock
def test_token_info_by_id_200(client):
    request = respx.get(f"{API_BASE_URL}/v1/streams/tokens/1/").respond(
        status_code=200,
        json={"key": "token", "is_active": True},
    )
    tokens = client.streams.tokens.get(token_id_or_key=1)
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()["key"] == "token"


@respx.mock
def test_token_info_by_key_200(client):
    request = respx.get(f"{API_BASE_URL}/v1/streams/tokens/token/").respond(
        status_code=200,
        json={"key": "token", "is_active": True},
    )
    tokens = client.streams.tokens.get(token_id_or_key="token")
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()["key"] == "token"


@respx.mock
@pytest.mark.asyncio
async def test_async_info_by_id_200(async_client):
    request = respx.get(f"{API_BASE_URL}/v1/streams/tokens/1/").respond(
        status_code=200,
        json={"key": "token", "is_active": True},
    )
    tokens = await async_client.streams.tokens.get(token_id_or_key=1)
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()["key"] == "token"


@respx.mock
@pytest.mark.asyncio
async def test_async_info_by_key_200(async_client):
    request = respx.get(f"{API_BASE_URL}/v1/streams/tokens/token/").respond(
        status_code=200,
        json={"key": "token", "is_active": True},
    )
    tokens = await async_client.streams.tokens.get(token_id_or_key="token")
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()["key"] == "token"


@respx.mock
def test_token_update_by_key_200(client):
    request = respx.patch(f"{API_BASE_URL}/v1/streams/tokens/token/").respond(
        status_code=200,
        json={"key": "token", "is_active": True},
    )
    tokens = client.streams.tokens.update(
        token_id_or_key="token", is_active=True
    )
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()["key"] == "token"
    assert tokens.json()["is_active"]


@respx.mock
def test_token_update_by_id_deactivate_200(client):
    request = respx.patch(f"{API_BASE_URL}/v1/streams/tokens/1/").respond(
        status_code=200,
        json={"key": "token", "is_active": False},
    )
    tokens = client.streams.tokens.update(token_id_or_key=1, is_active=False)
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()["key"] == "token"
    assert tokens.json()["is_active"] is False


@respx.mock
@pytest.mark.asyncio
async def test_async_update_by_key_200(async_client):
    request = respx.patch(f"{API_BASE_URL}/v1/streams/tokens/token/").respond(
        status_code=200,
        json={"key": "token", "is_active": True},
    )
    tokens = await async_client.streams.tokens.update(
        token_id_or_key="token", is_active=True
    )
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()["key"] == "token"
    assert tokens.json()["is_active"]


@respx.mock
@pytest.mark.asyncio
async def test_async_update_by_id_deactivate_200(async_client):
    request = respx.patch(f"{API_BASE_URL}/v1/streams/tokens/1/").respond(
        status_code=200,
        json={"key": "token", "is_active": False},
    )
    tokens = await async_client.streams.tokens.update(
        token_id_or_key=1, is_active=False
    )
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()["key"] == "token"
    assert tokens.json()["is_active"] is False


@respx.mock
def test_delete(client):
    request = respx.delete(f"{API_BASE_URL}/v1/streams/tokens/").respond(
        status_code=204
    )
    response = client.streams.tokens.delete_list()
    assert request.called
    assert response.status_code == 204


@respx.mock
def test_delete_permanent(client):
    request = respx.delete(
        f"{API_BASE_URL}/v1/streams/tokens/?permanent=true"
    ).respond(status_code=204)
    response = client.streams.tokens.delete_list(permanent=True)
    assert request.called
    assert response.status_code == 204


@respx.mock
@pytest.mark.asyncio
async def test_asyncs_delete(async_client):
    request = respx.delete(f"{API_BASE_URL}/v1/streams/tokens/").respond(
        status_code=204
    )
    response = await async_client.streams.tokens.delete_list()
    assert request.called
    assert response.status_code == 204


@respx.mock
@pytest.mark.asyncio
async def test_asyncs_delete_permanent(async_client):
    request = respx.delete(
        f"{API_BASE_URL}/v1/streams/tokens/?permanent=true"
    ).respond(status_code=204)
    response = await async_client.streams.tokens.delete_list(permanent=True)
    assert request.called
    assert response.status_code == 204


@respx.mock
def test_token_delete_by_key_204(client):
    request = respx.delete(f"{API_BASE_URL}/v1/streams/tokens/token/").respond(
        status_code=204
    )
    response = client.streams.tokens.delete(token_id_or_key="token")
    assert request.called
    assert response.status_code == 204


@respx.mock
def test_token_delete_by_id_204(client):
    request = respx.delete(f"{API_BASE_URL}/v1/streams/tokens/1/").respond(
        status_code=204
    )
    response = client.streams.tokens.delete(token_id_or_key=1)
    assert request.called
    assert response.status_code == 204


@respx.mock
@pytest.mark.asyncio
async def test_async_delete_by_key(async_client):
    request = respx.delete(f"{API_BASE_URL}/v1/streams/tokens/token/").respond(
        status_code=204
    )
    response = await async_client.streams.tokens.delete(
        token_id_or_key="token"
    )
    assert request.called
    assert response.status_code == 204


@respx.mock
@pytest.mark.asyncio
async def test_async_delete_by_id(async_client):
    request = respx.delete(f"{API_BASE_URL}/v1/streams/tokens/1/").respond(
        status_code=204
    )
    response = await async_client.streams.tokens.delete(token_id_or_key=1)
    assert request.called
    assert response.status_code == 204
