import pytest
import respx

from neuroio.constants import IAM_BASE_URL


@respx.mock
def test_me_username_200(client):
    request = respx.get(
        f"{IAM_BASE_URL}/v1/whoami/",
        status_code=200,
        content={"username": "name"},
    )
    response = client.whoami.me()
    assert request.called
    assert response.status_code == 200
    assert response.json()["username"] == "name"


@respx.mock
@pytest.mark.asyncio
async def test_async_me_username_200(async_client):
    request = respx.get(
        f"{IAM_BASE_URL}/v1/whoami/",
        status_code=200,
        content={"username": "name"},
    )
    response = await async_client.whoami.me()
    assert request.called
    assert response.status_code == 200
    assert response.json()["username"] == "name"
