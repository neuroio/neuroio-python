import pytest
import respx

from neuroio.constants import API_BASE_URL


@respx.mock
def test_sources_list_without_params_200(client):
    request = respx.get(
        f"{API_BASE_URL}/v1/sources/?q=&limit=20&offset=0",
        status_code=200,
        content={"results": [{"id": 1, "name": "source_name"}]},
    )
    response = client.sources.list()
    assert request.called
    assert response.status_code == 200
    assert response.json()["results"][0]["name"] == "source_name"


@respx.mock
def test_sources_list_with_params_200(client):
    request = respx.get(
        f"{API_BASE_URL}/v1/sources/?q=test&limit=20&offset=20",
        status_code=200,
        content={"results": [{"id": 1, "name": "source_name"}]},
    )
    response = client.sources.list(query="test", offset=20)
    assert request.called
    assert response.status_code == 200
    assert response.json()["results"][0]["name"] == "source_name"


@respx.mock
@pytest.mark.asyncio
async def test_async_list_without_params_200(async_client):
    request = respx.get(
        f"{API_BASE_URL}/v1/sources/?q=&limit=20&offset=0/",
        status_code=200,
        content={"results": [{"id": 1, "name": "source_name"}]},
    )
    response = await async_client.sources.list()
    assert request.called
    assert response.status_code == 200
    assert response.json()["results"][0]["name"] == "source_name"


@respx.mock
@pytest.mark.asyncio
async def test_async_list_without_params_200(async_client):
    request = respx.get(
        f"{API_BASE_URL}/v1/sources/?q=test&limit=20&offset=20",
        status_code=200,
        content={"results": [{"id": 1, "name": "source_name"}]},
    )
    response = await async_client.sources.list(query="test", offset=20)
    assert request.called
    assert response.status_code == 200
    assert response.json()["results"][0]["name"] == "source_name"
