from datetime import datetime

import pytest
import respx

from neuroio.constants import IAM_BASE_URL
from tests.utils import mock_query_params_all_combos


@respx.mock
def test_create_ok(client):
    request = respx.post(
        f"{IAM_BASE_URL}/v1/licenses/sources/",
        status_code=201,
        content={"name": "name", "entry_storage_days": 1, "is_active": True},
    )
    response = client.licenses.sources.create(
        name="name", entry_storage_days=1
    )

    assert request.called
    assert response.status_code == 201
    assert response.json()["is_active"] is True


@respx.mock
@pytest.mark.asyncio
async def test_async_create_ok(async_client):
    request = respx.post(
        f"{IAM_BASE_URL}/v1/licenses/sources/",
        status_code=201,
        content={"name": "name", "entry_storage_days": 1, "is_active": True},
    )
    response = await async_client.licenses.sources.create(
        name="name", entry_storage_days=1
    )

    assert request.called
    assert response.status_code == 201
    assert response.json()["is_active"] is True


@respx.mock
def test_get_by_id_200(client):
    request = respx.get(
        f"{IAM_BASE_URL}/v1/licenses/sources/1/",
        status_code=200,
        content={"id": 1, "name": "name"},
    )
    response = client.licenses.sources.get(id=1)
    assert request.called
    assert response.status_code == 200
    assert response.json()["name"] == "name"


@respx.mock
@pytest.mark.asyncio
async def test_async_get_by_id_200(async_client):
    request = respx.get(
        f"{IAM_BASE_URL}/v1/licenses/sources/1/",
        status_code=200,
        content={"id": 1, "name": "name"},
    )
    response = await async_client.licenses.sources.get(id=1)
    assert request.called
    assert response.status_code == 200
    assert response.json()["name"] == "name"


@respx.mock
def test_list_without_params200(client):
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/licenses/sources",
        "limit=20",
        "offset=0",
        "q=",
        content={"results": [{"id": 1, "name": "name"}]},
    )

    response = client.licenses.sources.list()
    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
def test_list_with_params200(client):
    date_str = "2018-06-29"
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/licenses/sources",
        "q=test",
        f"date_from={date_str}",
        f"date_to={date_str}",
        "limit=20",
        "offset=0",
        content={"results": [{"id": 1, "name": "name"}]},
    )

    response = client.licenses.sources.list(
        q="test", date_from=date_obj.date(), date_to=date_obj.date()
    )

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_list_without_params_200(async_client):
    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/licenses/sources",
        "limit=20",
        "offset=0",
        "q=",
        content={"results": [{"id": 1, "name": "name"}]},
    )
    response = await async_client.licenses.sources.list()
    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_list_with_params_200(async_client):
    date_str = "2018-06-29"
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    requests = mock_query_params_all_combos(
        f"{IAM_BASE_URL}/v1/licenses/sources",
        "q=test",
        f"date_from={date_str}",
        f"date_to={date_str}",
        "limit=20",
        "offset=0",
        content={"results": [{"id": 1, "name": "name"}]},
    )
    response = await async_client.licenses.sources.list(
        q="test", date_from=date_obj.date(), date_to=date_obj.date()
    )
    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
def test_update_by_id_deactivate_200(client):
    request = respx.patch(
        f"{IAM_BASE_URL}/v1/licenses/sources/1/",
        status_code=200,
        content={"id": 1, "name": "name", "is_active": False},
    )
    response = client.licenses.sources.update(
        id=1, name="name", is_active=False
    )
    assert request.called
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["is_active"] is False


@respx.mock
@pytest.mark.asyncio
async def test_async_update_by_id_deactivate_200(async_client):
    request = respx.patch(
        f"{IAM_BASE_URL}/v1/licenses/sources/1/",
        status_code=200,
        content={"id": 1, "name": "name", "is_active": False},
    )
    response = await async_client.licenses.sources.update(
        id=1, name="name", is_active=False
    )
    assert request.called
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["is_active"] is False
