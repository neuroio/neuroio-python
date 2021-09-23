import pytest
import respx

from neuroio.constants import API_BASE_URL, HttpMethod
from tests.utils import mock_query_params_all_combos


@respx.mock
def test_create_ok(client):
    request = respx.post(
        f"{API_BASE_URL}/v1/notifications/").respond(
        status_code=201,
        json={"id": 1, "name": "name"},
    )
    response = client.notifications.create(
        name="name", http_method=HttpMethod.GET, destination_url="url"
    )

    assert request.called
    assert response.status_code == 201
    assert response.json()["id"] == 1


@respx.mock
def test_create_failed(client):
    request = respx.post(f"{API_BASE_URL}/v1/notifications/").respond(status_code=400)
    response = client.notifications.create(
        name="name", http_method=HttpMethod.GET, destination_url="url"
    )

    assert request.called
    assert response.status_code == 400


@respx.mock
@pytest.mark.asyncio
async def test_async_create_ok(async_client):
    request = respx.post(
        f"{API_BASE_URL}/v1/notifications/").respond(
        status_code=201,
        json={"id": 1, "name": "name"},
    )
    response = await async_client.notifications.create(
        name="name", http_method=HttpMethod.GET, destination_url="url"
    )

    assert request.called
    assert response.status_code == 201
    assert response.json()["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_create_failed(async_client):
    request = respx.post(f"{API_BASE_URL}/v1/notifications/").respond(status_code=400)
    response = await async_client.notifications.create(
        name="name", http_method=HttpMethod.GET, destination_url="url"
    )

    assert request.called
    assert response.status_code == 400


@respx.mock
def test_list_without_params(client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/notifications",
        "limit=20",
        "offset=0",
        json={"results": [{"id": 1, "name": "name"}]},
    )
    response = client.notifications.list()

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
def test_list_with_params(client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/notifications",
        "limit=20",
        "offset=20",
        "q=test",
        json={"results": [{"id": 1, "name": "name"}]},
    )
    response = client.notifications.list(q="test", offset=20)

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_without_params(async_client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/notifications",
        "limit=20",
        "offset=0",
        json={"results": [{"id": 1, "name": "name"}]},
    )
    response = await async_client.notifications.list()

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_with_params(async_client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/notifications",
        "limit=20",
        "offset=20",
        "q=test",
        json={"results": [{"id": 1, "name": "name"}]},
    )
    response = await async_client.notifications.list(q="test", offset=20)

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
def test_get_ok(client):
    request = respx.get(
        f"{API_BASE_URL}/v1/notifications/1/").respond(
        status_code=200,
        json={"name": "name", "id": 1},
    )
    response = client.notifications.get(id=1)

    assert request.called
    assert response.status_code == 200
    assert response.json()["id"] == 1


@respx.mock
def test_get_failed(client):
    request = respx.get(f"{API_BASE_URL}/v1/notifications/1/").respond(status_code=404)
    response = client.notifications.get(id=1)

    assert request.called
    assert response.status_code == 404


@respx.mock
@pytest.mark.asyncio
async def test_async_get_ok(async_client):
    request = respx.get(
        f"{API_BASE_URL}/v1/notifications/1/").respond(
        status_code=200,
        json={"name": "name", "id": 1},
    )
    response = await async_client.notifications.get(id=1)

    assert request.called
    assert response.status_code == 200
    assert response.json()["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_get_failed(async_client):
    request = respx.get(f"{API_BASE_URL}/v1/notifications/1/").respond(status_code=404)
    response = await async_client.notifications.get(id=1)

    assert request.called
    assert response.status_code == 404


@respx.mock
def test_update_ok(client):
    request = respx.patch(
        f"{API_BASE_URL}/v1/notifications/1/").respond(
        status_code=200,
        json={"name": "new_name", "id": 1},
    )
    response = client.notifications.update(
        id=1,
        name="new_name",
        http_method=HttpMethod.GET,
        destination_url="url",
    )

    assert request.called
    assert response.status_code == 200
    assert response.json()["name"] == "new_name"


@respx.mock
def test_update_failed(client):
    request = respx.patch(
        f"{API_BASE_URL}/v1/notifications/1/").respond(status_code=404
    )
    response = client.notifications.update(
        id=1,
        name="new_name",
        http_method=HttpMethod.GET,
        destination_url="url",
    )

    assert request.called
    assert response.status_code == 404


@respx.mock
@pytest.mark.asyncio
async def test_async_update_ok(async_client):
    request = respx.patch(
        f"{API_BASE_URL}/v1/notifications/1/").respond(
        status_code=200,
        json={"name": "new_name", "id": 1},
    )
    response = await async_client.notifications.update(
        id=1,
        name="new_name",
        http_method=HttpMethod.GET,
        destination_url="url",
    )

    assert request.called
    assert response.status_code == 200
    assert response.json()["name"] == "new_name"


@respx.mock
@pytest.mark.asyncio
async def test_async_update_failed(async_client):
    request = respx.patch(
        f"{API_BASE_URL}/v1/notifications/1/").respond(status_code=404
    )
    response = await async_client.notifications.update(
        id=1,
        name="new_name",
        http_method=HttpMethod.GET,
        destination_url="url",
    )

    assert request.called
    assert response.status_code == 404


@respx.mock
def test_delete_ok(client):
    request = respx.delete(
        f"{API_BASE_URL}/v1/notifications/1/").respond(status_code=204
    )
    response = client.notifications.delete(id=1)

    assert request.called
    assert response.status_code == 204


@respx.mock
def test_delete_failed(client):
    request = respx.delete(
        f"{API_BASE_URL}/v1/notifications/1/").respond(status_code=404
    )
    response = client.notifications.delete(id=1)

    assert request.called
    assert response.status_code == 404


@respx.mock
@pytest.mark.asyncio
async def test_async_delete_ok(async_client):
    request = respx.delete(
        f"{API_BASE_URL}/v1/notifications/1/").respond(status_code=204
    )
    response = await async_client.notifications.delete(id=1)

    assert request.called
    assert response.status_code == 204


@respx.mock
@pytest.mark.asyncio
async def test_async_delete_failed(async_client):
    request = respx.delete(
        f"{API_BASE_URL}/v1/notifications/1/").respond(status_code=404
    )
    response = await async_client.notifications.delete(id=1)

    assert request.called
    assert response.status_code == 404
