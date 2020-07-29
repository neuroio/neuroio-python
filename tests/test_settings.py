import pytest
import respx

from neuroio.constants import API_BASE_URL


@respx.mock
def test_get_200(client):
    request = respx.get(
        f"{API_BASE_URL}/v1/settings/thresholds/",
        status_code=200,
        content={"exact": 1, "ha": 1, "junk": 1},
    )
    response = client.settings.get()

    assert request.called
    assert response.status_code == 200
    assert response.json() == {"exact": 1, "ha": 1, "junk": 1}


@respx.mock
@pytest.mark.asyncio
async def test_async_get_200(async_client):
    request = respx.get(
        f"{API_BASE_URL}/v1/settings/thresholds/",
        status_code=200,
        content={"exact": 1, "ha": 1, "junk": 1},
    )
    response = await async_client.settings.get()

    assert request.called
    assert response.status_code == 200
    assert response.json() == {"exact": 1, "ha": 1, "junk": 1}


@respx.mock
def test_update_200(client):
    request = respx.patch(
        f"{API_BASE_URL}/v1/settings/thresholds/",
        status_code=200,
        content={"exact": 2, "ha": 2, "junk": 2},
    )
    response = client.settings.update(2, 2, 2)

    assert request.called
    assert response.status_code == 200
    assert response.json() == {"exact": 2, "ha": 2, "junk": 2}


@respx.mock
@pytest.mark.asyncio
async def test_async_update_200(async_client):
    request = respx.patch(
        f"{API_BASE_URL}/v1/settings/thresholds/",
        status_code=200,
        content={"exact": 2, "ha": 2, "junk": 2},
    )
    response = await async_client.settings.update(2, 2, 2)

    assert request.called
    assert response.status_code == 200
    assert response.json() == {"exact": 2, "ha": 2, "junk": 2}


@respx.mock
def test_reset_200(client):
    request = respx.post(
        f"{API_BASE_URL}/v1/settings/thresholds/reset/", status_code=200
    )
    response = client.settings.reset()

    assert request.called
    assert response.status_code == 200


@respx.mock
@pytest.mark.asyncio
async def test_async_reset_200(async_client):
    request = respx.post(
        f"{API_BASE_URL}/v1/settings/thresholds/reset/", status_code=200
    )
    response = await async_client.settings.reset()

    assert request.called
    assert response.status_code == 200
