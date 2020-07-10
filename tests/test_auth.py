import pytest
import respx

from neuroio.constants import API_BASE_URL


@respx.mock
def test_login_200(client):
    request = respx.post(
        f"{API_BASE_URL}/v1/login/", status_code=200, content={"token": "key"}
    )
    login_response = client.auth.login(
        username="helloworld", password="superpwd"
    )
    assert request.called
    assert login_response.status_code == 200
    assert login_response.json()["token"] == "key"


@respx.mock
@pytest.mark.asyncio
async def test_async_login_200(async_client):
    request = respx.post(
        f"{API_BASE_URL}/v1/login/", status_code=200, content={"token": "key"}
    )
    login_response = await async_client.auth.login(
        username="helloworld", password="superpwd"
    )
    assert request.called
    assert login_response.status_code == 200
    assert login_response.json()["token"] == "key"


@respx.mock
def test_login_permanent_200(client):
    request = respx.post(
        f"{API_BASE_URL}/v1/login/permanent/",
        status_code=200,
        content={"token": "key"},
    )
    login_response = client.auth.login_permanent(
        username="helloworld", password="superpwd"
    )
    assert request.called
    assert login_response.status_code == 200
    assert login_response.json()["token"] == "key"


@respx.mock
@pytest.mark.asyncio
async def test_async_login_permanent_200(async_client):
    request = respx.post(
        f"{API_BASE_URL}/v1/login/permanent/",
        status_code=200,
        content={"token": "key"},
    )
    login_response = await async_client.auth.login_permanent(
        username="helloworld", password="superpwd"
    )
    assert request.called
    assert login_response.status_code == 200
    assert login_response.json()["token"] == "key"
