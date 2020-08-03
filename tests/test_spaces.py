import pytest
import respx

from neuroio.constants import API_BASE_URL


@respx.mock
def test_create_ok(client):
    request = respx.post(
        f"{API_BASE_URL}/v1/spaces/",
        status_code=201,
        content={"id": 1, "name": "name"},
    )
    response = client.spaces.create(name="name")

    assert request.called
    assert response.status_code == 201
    assert response.json()["name"] == "name"


@respx.mock
def test_create_failed(client):
    request = respx.post(f"{API_BASE_URL}/v1/spaces/", status_code=400)
    response = client.spaces.create(name="name")

    assert request.called
    assert response.status_code == 400


@respx.mock
@pytest.mark.asyncio
async def test_async_create_ok(async_client):
    request = respx.post(
        f"{API_BASE_URL}/v1/spaces/",
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
    request = respx.post(f"{API_BASE_URL}/v1/spaces/", status_code=400)
    response = await async_client.spaces.create(name="name")

    assert request.called
    assert response.status_code == 400
