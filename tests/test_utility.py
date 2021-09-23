import pytest
import respx

from neuroio.constants import API_BASE_URL


@respx.mock
def test_test_compare_200(client):
    request = respx.post(
        f"{API_BASE_URL}/v1/utility/compare/").respond(status_code=200
    )
    response = client.utility.compare(b"image1", b"image2")

    assert request.called
    assert response.status_code == 200


@respx.mock
@pytest.mark.asyncio
async def test_async_compare_200(async_client):
    request = respx.post(
        f"{API_BASE_URL}/v1/utility/compare/").respond(status_code=200
    )
    response = await async_client.utility.compare(b"image1", b"image2")

    assert request.called
    assert response.status_code == 200


@respx.mock
def test_asm_200(client):
    request = respx.post(f"{API_BASE_URL}/v1/utility/asm/").respond(status_code=200)
    response = client.utility.asm(b"image")

    assert request.called
    assert response.status_code == 200


@respx.mock
@pytest.mark.asyncio
async def test_async_asm_200(async_client):
    request = respx.post(f"{API_BASE_URL}/v1/utility/asm/").respond(status_code=200)
    response = await async_client.utility.asm(b"image")

    assert request.called
    assert response.status_code == 200
