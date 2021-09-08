import pytest
import respx

from neuroio.constants import IAM_BASE_URL
from tests.utils import mock_query_params_all_combos


@respx.mock
def test_create_ok(client):
    request = respx.post(
        f"{IAM_BASE_URL}/v1/spaces/",
        status_code=201,
        content={"id": 1, "name": "name"},
    )
    response = client.spaces.create(name="name")

    assert request.called
    assert response.status_code == 201
    assert response.json()["name"] == "name"


@respx.mock
def test_create_failed(client):
    request = respx.post(f"{IAM_BASE_URL}/v1/spaces/", status_code=400)
    response = client.spaces.create(name="name")

    assert request.called
    assert response.status_code == 400


@respx.mock
@pytest.mark.asyncio
async def test_async_create_ok(async_client):
    request = respx.post(
        f"{IAM_BASE_URL}/v1/spaces/",
        status_code=201,
        content={"id": 1, "name": "name"},
    )
    response = await async_client.spaces.create(name="name")

    assert request.called
    assert response.status_code == 201
    assert response.json()["name"] == "name"


@respx.mock
@pytest.mark.asyncio
async def test_async_create_failed(async_client):
    request = respx.post(f"{IAM_BASE_URL}/v1/spaces/", status_code=400)
    response = await async_client.spaces.create(name="name")

    assert request.called
    assert response.status_code == 400


@respx.mock
def test_list_without_params(client):
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/spaces",
        "limit=20",
        "offset=0",
        "q=",
        content={"results": [{"id": 1, "name": "name"}]},
    )
    response = client.spaces.list()

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
def test_spaces_full_list(client):
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/lists/spaces",
        content={"results": [{"id": 1, "name": "name"}]},
    )
    response = client.spaces.spaces_full_list()

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
def test_list_with_params(client):
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/spaces",
        "limit=20",
        "offset=20",
        "q=test",
        content={"results": [{"id": 1, "name": "name"}]},
    )
    response = client.spaces.list(q="test", offset=20)

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_list_without_params(async_client):
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/spaces",
        "limit=20",
        "offset=0",
        "q=",
        content={"results": [{"id": 1, "name": "name"}]},
    )
    response = await async_client.spaces.list()

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_spaces_full_list(async_client):
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/lists/spaces/",
        content={"results": [{"id": 1, "name": "name"}]},
    )
    response = await async_client.spaces.spaces_full_list()

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_list_with_params(async_client):
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/spaces",
        "limit=20",
        "offset=20",
        "q=test",
        content={"results": [{"id": 1, "name": "name"}]},
    )
    response = await async_client.spaces.list(q="test", offset=20)

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
def test_get_ok(client):
    request = respx.get(
        f"{IAM_BASE_URL}/v1/spaces/1/",
        status_code=200,
        content={"id": 1, "name": "name"},
    )
    response = client.spaces.get(id=1)

    assert request.called
    assert response.status_code == 200
    assert response.json()["id"] == 1


@respx.mock
def test_get_not_found(client):
    request = respx.get(f"{IAM_BASE_URL}/v1/spaces/1/", status_code=404)
    response = client.spaces.get(id=1)

    assert request.called
    assert response.status_code == 404


@respx.mock
@pytest.mark.asyncio
async def test_async_get_ok(async_client):
    request = respx.get(
        f"{IAM_BASE_URL}/v1/spaces/1/",
        status_code=200,
        content={"id": 1, "name": "name"},
    )
    response = await async_client.spaces.get(id=1)

    assert request.called
    assert response.status_code == 200
    assert response.json()["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_get_not_found(async_client):
    request = respx.get(f"{IAM_BASE_URL}/v1/spaces/1/", status_code=404)
    response = await async_client.spaces.get(id=1)

    assert request.called
    assert response.status_code == 404


@respx.mock
def test_update_ok(client):
    request = respx.patch(
        f"{IAM_BASE_URL}/v1/spaces/1/",
        status_code=200,
        content={"id": 1, "name": "new_name"},
    )
    response = client.spaces.update(id=1, name="new_name")

    assert request.called
    assert response.status_code == 200
    assert response.json()["name"] == "new_name"


@respx.mock
@pytest.mark.asyncio
async def test_async_update_ok(async_client):
    request = respx.patch(
        f"{IAM_BASE_URL}/v1/spaces/1/",
        status_code=200,
        content={"id": 1, "name": "new_name"},
    )
    response = await async_client.spaces.update(id=1, name="new_name")

    assert request.called
    assert response.status_code == 200
    assert response.json()["name"] == "new_name"


@respx.mock
def test_delete_ok(client):
    request = respx.delete(f"{IAM_BASE_URL}/v1/spaces/1/", status_code=202)
    response = client.spaces.delete(id=1)

    assert request.called
    assert response.status_code == 202


@respx.mock
@pytest.mark.asyncio
async def test_async_delete_ok(async_client):
    request = respx.delete(f"{IAM_BASE_URL}/v1/spaces/1/", status_code=202)
    response = await async_client.spaces.delete(id=1)

    assert request.called
    assert response.status_code == 202


@respx.mock
def test_token_create_ok(client):
    request = respx.post(
        f"{IAM_BASE_URL}/v1/spaces/1/tokens/",
        status_code=201,
        content={"is_active": True, "key": "key"},
    )
    response = client.spaces.token(id=1)

    assert request.called
    assert response.status_code == 201
    assert response.json()["key"] == "key"


@respx.mock
def test_token_create_failed(client):
    request = respx.post(
        f"{IAM_BASE_URL}/v1/spaces/1/tokens/", status_code=400
    )
    response = client.spaces.token(id=1)

    assert request.called
    assert response.status_code == 400


@respx.mock
@pytest.mark.asyncio
async def test_async_token_create(async_client):
    request = respx.post(
        f"{IAM_BASE_URL}/v1/spaces/1/tokens/",
        status_code=201,
        content={"is_active": True, "key": "key"},
    )
    response = await async_client.spaces.token(id=1)

    assert request.called
    assert response.status_code == 201
    assert response.json()["key"] == "key"


@respx.mock
@pytest.mark.asyncio
async def test_async_token_create_failed(async_client):
    request = respx.post(
        f"{IAM_BASE_URL}/v1/spaces/1/tokens/", status_code=400
    )
    response = await async_client.spaces.token(id=1)

    assert request.called
    assert response.status_code == 400
