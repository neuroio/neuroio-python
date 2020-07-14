from datetime import datetime

import pytest
import respx

from neuroio.constants import API_BASE_URL


@respx.mock
def test_list_without_params200(client):
    request = respx.get(
        f"{API_BASE_URL}/v1/entries/?limit=20&offset=0",
        status_code=200,
        content={"results": [{"id": 1, "pid": "or"}]},
    )
    response = client.entries.list()
    assert request.called
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
def test_list_with_params200(client):
    date_str = "2018-06-29"
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    request = respx.get(
        f"{API_BASE_URL}/v1/entries/?source=1,2,3&date_from={date_str}"
        f"&limit=20&offset=0".replace(",", "%2C"),
        status_code=200,
        content={"results": [{"id": 1, "pid": "or"}]},
    )
    response = client.entries.list(source=[1, 2, 3], date_from=date_obj.date())

    assert request.called
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_list_without_params_200(async_client):
    request = respx.get(
        f"{API_BASE_URL}/v1/entries/?limit=20&offset=0",
        status_code=200,
        content={"results": [{"id": 1, "pid": "or"}]},
    )
    response = await async_client.entries.list()
    assert request.called
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1


@respx.mock
@pytest.mark.asyncio
async def test_async_list_with_params_200(async_client):
    date_str = "2018-06-29"
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    request = respx.get(
        f"{API_BASE_URL}/v1/entries/?source=1,2,3&date_from={date_str}"
        f"&limit=20&offset=0".replace(",", "%2C"),
        status_code=200,
        content={"results": [{"id": 1, "pid": "or"}]},
    )
    response = await async_client.entries.list(
        source=[1, 2, 3], date_from=date_obj.date()
    )
    assert request.called
    assert response.status_code == 200
    assert response.json()["results"][0]["id"] == 1
