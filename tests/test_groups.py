import pytest
import respx

from neuroio.constants import API_BASE_URL
from tests.utils import mock_query_params_all_combos


@respx.mock
def test_create(client):
    request = respx.post(
        f"{API_BASE_URL}/v1/groups/persons/",
        status_code=201,
        content={"id": 1, "name": "test_name"},
    )
    response = client.groups.create("test_name")

    assert request.called
    assert response.status_code == 201
    assert response.json()["name"] == "test_name"


@respx.mock
@pytest.mark.asyncio
async def test_async_create(async_client):
    request = respx.post(
        f"{API_BASE_URL}/v1/groups/persons/",
        status_code=201,
        content={"id": 1, "name": "test_name"},
    )
    response = await async_client.groups.create("test_name")

    assert request.called
    assert response.status_code == 201
    assert response.json()["name"] == "test_name"


@respx.mock
def test_list_without_params_200(client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/groups/persons", "limit=20", "offset=0"
    )
    response = client.groups.list()

    assert any([request.called for request in requests])
    assert response.status_code == 200


@respx.mock
def test_list_with_params_200(client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/groups/persons",
        "limit=20",
        "offset=0",
        "pids_include=pid1,pid2".replace(",", "%2C"),
        "q=test",
    )
    response = client.groups.list(pids_include=["pid1", "pid2"], q="test")

    assert any([request.called for request in requests])
    assert response.status_code == 200


@respx.mock
@pytest.mark.asyncio
async def test_async_list_without_params_200(async_client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/groups/persons", "limit=20", "offset=0"
    )
    response = await async_client.groups.list()

    assert any([request.called for request in requests])
    assert response.status_code == 200


@respx.mock
@pytest.mark.asyncio
async def test_async_list_with_params_200(async_client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/groups/persons",
        "limit=20",
        "offset=0",
        "pids_include=pid1,pid2".replace(",", "%2C"),
        "q=test",
    )
    response = await async_client.groups.list(
        pids_include=["pid1", "pid2"], q="test"
    )

    assert any([request.called for request in requests])
    assert response.status_code == 200


@respx.mock
def test_get_200(client):
    request = respx.get(
        f"{API_BASE_URL}/v1/groups/persons/1/",
        status_code=200,
        content={"id": 1, "name": "test"},
    )
    response = client.groups.get(1)

    assert request.called
    assert response.status_code == 200
    assert response.json()["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_get_200(async_client):
    request = respx.get(
        f"{API_BASE_URL}/v1/groups/persons/1/",
        status_code=200,
        content={"id": 1, "name": "test"},
    )
    response = await async_client.groups.get(1)

    assert request.called
    assert response.status_code == 200
    assert response.json()["id"] == 1


@respx.mock
def test_update_200(client):
    request = respx.patch(
        f"{API_BASE_URL}/v1/groups/persons/1/",
        status_code=200,
        content={"id": 1, "name": "new_name"},
    )
    response = client.groups.update(1, name="new_name")

    assert request.called
    assert response.status_code == 200
    assert response.json()["name"] == "new_name"


@respx.mock
@pytest.mark.asyncio
async def test_async_update_200(async_client):
    request = respx.patch(
        f"{API_BASE_URL}/v1/groups/persons/1/",
        status_code=200,
        content={"id": 1, "name": "new_name"},
    )
    response = await async_client.groups.update(1, name="new_name")

    assert request.called
    assert response.status_code == 200
    assert response.json()["name"] == "new_name"


@respx.mock
def test_delete_204(client):
    request = respx.delete(
        f"{API_BASE_URL}/v1/groups/persons/1/", status_code=204
    )
    response = client.groups.delete(1)

    assert request.called
    assert response.status_code == 204


@respx.mock
@pytest.mark.asyncio
async def test_async_delete_204(async_client):
    request = respx.delete(
        f"{API_BASE_URL}/v1/groups/persons/1/", status_code=204
    )
    response = await async_client.groups.delete(1)

    assert request.called
    assert response.status_code == 204


@respx.mock
def test_persons_list_without_params_200(client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/groups/persons/1/pids",
        "limit=20",
        "offset=0",
        content={
            "count": 1,
            "results": [{"pid": "pid", "pid_source": "default"}],
        },
    )
    response = client.groups.persons(1)

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["pid"] == "pid"


@respx.mock
def test_persons_list_with_params_200(client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/groups/persons/1/pids",
        "limit=20",
        "offset=0",
        "pids=pid1,pid2".replace(",", "%2C"),
        content={
            "count": 1,
            "results": [{"pid": "pid", "pid_source": "default"}],
        },
    )
    response = client.groups.persons(1, pids=["pid1", "pid2"])

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["pid"] == "pid"


@respx.mock
@pytest.mark.asyncio
async def test_async_persons_list_without_params_200(async_client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/groups/persons/1/pids",
        "limit=20",
        "offset=0",
        content={
            "count": 1,
            "results": [{"pid": "pid", "pid_source": "default"}],
        },
    )
    response = await async_client.groups.persons(1)

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["pid"] == "pid"


@respx.mock
@pytest.mark.asyncio
async def test_async_persons_list_with_params_200(async_client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/groups/persons/1/pids",
        "limit=20",
        "offset=0",
        "pids=pid1,pid2".replace(",", "%2C"),
        content={
            "count": 1,
            "results": [{"pid": "pid", "pid_source": "default"}],
        },
    )
    response = await async_client.groups.persons(1, pids=["pid1", "pid2"])

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["pid"] == "pid"


@respx.mock
def test_add_persons_200(client):
    request = respx.post(
        f"{API_BASE_URL}/v1/groups/persons/pids/", status_code=200
    )
    response = client.groups.add(pids=["pid"], groups_ids=[1, 2])

    assert request.called
    assert response.status_code == 200


@respx.mock
@pytest.mark.asyncio
async def test_async_add_persons_200(async_client):
    request = respx.post(
        f"{API_BASE_URL}/v1/groups/persons/pids/", status_code=200
    )
    response = await async_client.groups.add(pids=["pid"], groups_ids=[1, 2])

    assert request.called
    assert response.status_code == 200


@respx.mock
def test_remove_persons_200(client):
    request = respx.delete(
        f"{API_BASE_URL}/v1/groups/persons/pids/", status_code=200
    )
    response = client.groups.remove(pids=["pid"], groups_ids=[1, 2])

    assert request.called
    assert response.status_code == 200


@respx.mock
@pytest.mark.asyncio
async def test_async_remove_persons_200(async_client):
    request = respx.delete(
        f"{API_BASE_URL}/v1/groups/persons/pids/", status_code=200
    )
    response = await async_client.groups.remove(
        pids=["pid"], groups_ids=[1, 2]
    )

    assert request.called
    assert response.status_code == 200
