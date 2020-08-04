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


@respx.mock
def test_token_info_by_id_200(client):
    request = respx.get(
        f"{API_BASE_URL}/v1/users/tokens/1/",
        status_code=200,
        content={"key": "token", "is_active": True},
    )
    tokens = client.users.token_info(token_id_or_key=1)
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()["key"] == "token"


@respx.mock
def test_token_info_by_key_200(client):
    request = respx.get(
        f"{API_BASE_URL}/v1/users/tokens/token/",
        status_code=200,
        content={"key": "token", "is_active": True},
    )
    tokens = client.users.token_info(token_id_or_key="token")
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()["key"] == "token"


@respx.mock
@pytest.mark.asyncio
async def test_async_token_info_by_id_200(async_client):
    request = respx.get(
        f"{API_BASE_URL}/v1/users/tokens/1/",
        status_code=200,
        content={"key": "token", "is_active": True},
    )
    tokens = await async_client.users.token_info(token_id_or_key=1)
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()["key"] == "token"


@respx.mock
@pytest.mark.asyncio
async def test_async_token_info_by_key_200(async_client):
    request = respx.get(
        f"{API_BASE_URL}/v1/users/tokens/token/",
        status_code=200,
        content={"key": "token", "is_active": True},
    )
    tokens = await async_client.users.token_info(token_id_or_key="token")
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()["key"] == "token"


@respx.mock
def test_token_update_by_key_200(client):
    request = respx.patch(
        f"{API_BASE_URL}/v1/users/tokens/token/",
        status_code=200,
        content={"key": "token", "is_active": True},
    )
    tokens = client.users.token_update(token_id_or_key="token", is_active=True)
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()["key"] == "token"
    assert tokens.json()["is_active"]


@respx.mock
def test_token_update_by_id_deactivate_200(client):
    request = respx.patch(
        f"{API_BASE_URL}/v1/users/tokens/1/",
        status_code=200,
        content={"key": "token", "is_active": False},
    )
    tokens = client.users.token_update(token_id_or_key=1, is_active=False)
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()["key"] == "token"
    assert tokens.json()["is_active"] is False


@respx.mock
@pytest.mark.asyncio
async def test_async_token_update_by_key_200(async_client):
    request = respx.patch(
        f"{API_BASE_URL}/v1/users/tokens/token/",
        status_code=200,
        content={"key": "token", "is_active": True},
    )
    tokens = await async_client.users.token_update(
        token_id_or_key="token", is_active=True
    )
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()["key"] == "token"
    assert tokens.json()["is_active"]


@respx.mock
@pytest.mark.asyncio
async def test_async_token_update_by_id_deactivate_200(async_client):
    request = respx.patch(
        f"{API_BASE_URL}/v1/users/tokens/1/",
        status_code=200,
        content={"key": "token", "is_active": False},
    )
    tokens = await async_client.users.token_update(
        token_id_or_key=1, is_active=False
    )
    assert request.called
    assert tokens.status_code == 200
    assert tokens.json()["key"] == "token"
    assert tokens.json()["is_active"] is False


@respx.mock
def test_tokens_delete(client):
    request = respx.delete(f"{API_BASE_URL}/v1/users/tokens/", status_code=204)
    response = client.users.tokens_delete()
    assert request.called
    assert response.status_code == 204


@respx.mock
def test_tokens_delete_permanent(client):
    request = respx.delete(
        f"{API_BASE_URL}/v1/users/tokens/?permanent=true", status_code=204
    )
    response = client.users.tokens_delete(permanent=True)
    assert request.called
    assert response.status_code == 204


@respx.mock
@pytest.mark.asyncio
async def test_async_tokens_delete(async_client):
    request = respx.delete(f"{API_BASE_URL}/v1/users/tokens/", status_code=204)
    response = await async_client.users.tokens_delete()
    assert request.called
    assert response.status_code == 204


@respx.mock
@pytest.mark.asyncio
async def test_async_tokens_delete_permanent(async_client):
    request = respx.delete(
        f"{API_BASE_URL}/v1/users/tokens/?permanent=true", status_code=204
    )
    response = await async_client.users.tokens_delete(permanent=True)
    assert request.called
    assert response.status_code == 204


@respx.mock
def test_token_delete_by_key_204(client):
    request = respx.delete(
        f"{API_BASE_URL}/v1/users/tokens/token/", status_code=204
    )
    response = client.users.token_delete(token_id_or_key="token")
    assert request.called
    assert response.status_code == 204


@respx.mock
def test_token_delete_by_id_204(client):
    request = respx.delete(
        f"{API_BASE_URL}/v1/users/tokens/1/", status_code=204
    )
    response = client.users.token_delete(token_id_or_key=1)
    assert request.called
    assert response.status_code == 204


@respx.mock
@pytest.mark.asyncio
async def test_async_token_delete_by_key(async_client):
    request = respx.delete(
        f"{API_BASE_URL}/v1/users/tokens/token/", status_code=204
    )
    response = await async_client.users.token_delete(token_id_or_key="token")
    assert request.called
    assert response.status_code == 204


@respx.mock
@pytest.mark.asyncio
async def test_async_token_delete_by_id(async_client):
    request = respx.delete(
        f"{API_BASE_URL}/v1/users/tokens/1/", status_code=204
    )
    response = await async_client.users.token_delete(token_id_or_key=1)
    assert request.called
    assert response.status_code == 204


@respx.mock
def test_me_username_200(client):
    request = respx.get(
        f"{API_BASE_URL}/v1/users/me/",
        status_code=200,
        content={"username": "name"},
    )
    response = client.users.me()
    assert request.called
    assert response.status_code == 200
    assert response.json()["username"] == "name"


@respx.mock
@pytest.mark.asyncio
async def test_async_me_username_200(async_client):
    request = respx.get(
        f"{API_BASE_URL}/v1/users/me/",
        status_code=200,
        content={"username": "name"},
    )
    response = await async_client.users.me()
    assert request.called
    assert response.status_code == 200
    assert response.json()["username"] == "name"
