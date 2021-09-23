from datetime import datetime

import pytest
import respx

from neuroio.constants import API_BASE_URL
from tests.utils import mock_query_params_all_combos


@respx.mock
def test_list_without_params200(client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/entries",
        "limit=20",
        "offset=0",
        json={"results": [{"id": 1, "pid": "pid"}]},
    )

    response = client.entries.list()
    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
def test_list_with_params200(client):
    date_str = "2018-06-29"
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/entries",
        "sources_ids=1,2,3".replace(",", "%2C"),
        f"date_from={date_str}",
        "limit=20",
        "offset=0",
        json={"results": [{"id": 1, "pid": "pid"}]},
    )

    response = client.entries.list(
        sources_ids=[1, 2, 3], date_from=date_obj.date()
    )

    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_list_without_params_200(async_client):
    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/entries",
        "limit=20",
        "offset=0",
        json={"results": [{"id": 1, "pid": "pid"}]},
    )
    response = await async_client.entries.list()
    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_list_with_params_200(async_client):
    date_str = "2018-06-29"
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    requests = mock_query_params_all_combos(
        f"{API_BASE_URL}/v1/entries",
        "sources_ids=1,2,3".replace(",", "%2C"),
        f"date_from={date_str}",
        "limit=20",
        "offset=0",
        json={"results": [{"id": 1, "pid": "pid"}]},
    )
    response = await async_client.entries.list(
        sources_ids=[1, 2, 3], date_from=date_obj.date()
    )
    assert any([request.called for request in requests])
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
def test_retrieve_200(client):
    request = respx.get(
        f"{API_BASE_URL}/v1/entries/stats/pid/pid/").respond(
        status_code=200,
        json={"id": 1, "pid": "pid", "age": 27},
    )
    response = client.entries.get(pid="pid")

    assert request.called
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["age"] == 27


@respx.mock
def test_retrieve_404(client):
    request = respx.get(
        f"{API_BASE_URL}/v1/entries/stats/pid/pid/").respond(status_code=404
    )
    response = client.entries.get(pid="pid")

    assert request.called
    assert response.status_code == 404


@respx.mock
@pytest.mark.asyncio
async def test_async_retrieve_200(async_client):
    request = respx.get(
        f"{API_BASE_URL}/v1/entries/stats/pid/pid/").respond(
        status_code=200,
        json={"id": 1, "pid": "pid", "age": 27},
    )
    response = await async_client.entries.get(pid="pid")
    assert request.called
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["age"] == 27


@respx.mock
@pytest.mark.asyncio
async def test_async_retrieve_404(async_client):
    request = respx.get(
        f"{API_BASE_URL}/v1/entries/stats/pid/pid/").respond(status_code=404
    )
    response = await async_client.entries.get(pid="pid")
    assert request.called
    assert response.status_code == 404


@respx.mock
def test_delete_204(client):
    request = respx.delete(f"{API_BASE_URL}/v1/entries/1/").respond(status_code=204)
    response = client.entries.delete(id=1)
    assert request.called
    assert response.status_code == 204


@respx.mock
def test_delete_400(client):
    request = respx.delete(f"{API_BASE_URL}/v1/entries/1/").respond(status_code=400)
    response = client.entries.delete(id=1)
    assert request.called
    assert response.status_code == 400


@respx.mock
@pytest.mark.asyncio
async def test_async_delete_204(async_client):
    request = respx.delete(f"{API_BASE_URL}/v1/entries/1/").respond(status_code=204)
    response = await async_client.entries.delete(id=1)
    assert request.called
    assert response.status_code == 204


@respx.mock
@pytest.mark.asyncio
async def test_async_delete_400(async_client):
    request = respx.delete(f"{API_BASE_URL}/v1/entries/1/").respond(status_code=400)
    response = await async_client.entries.delete(id=1)
    assert request.called
    assert response.status_code == 400
