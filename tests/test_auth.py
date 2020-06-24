import pytest
import respx

from neuroio import AsyncClient, Client
from neuroio.constants import API_BASE_URL


@respx.mock
def test_login_200():
    neuroio = Client()
    request = respx.post(
        f"{API_BASE_URL}/v1/login/", status_code=200, content={"token": "key"}
    )
    login_response = neuroio.auth.login(
        username="helloworld", password="superpwd"
    )
    assert request.called
    assert login_response.status_code == 200
    assert login_response.json()["token"] == "key"


@respx.mock
@pytest.mark.asyncio
async def test_async_login_200():
    neuroio = AsyncClient(api_token="anotherone")
    request = respx.post(
        f"{API_BASE_URL}/v1/login/", status_code=200, content={"token": "key"}
    )
    login_response = await neuroio.auth.login(
        username="helloworld", password="superpwd"
    )
    assert request.called
    assert login_response.status_code == 200
    assert login_response.json()["token"] == "key"
