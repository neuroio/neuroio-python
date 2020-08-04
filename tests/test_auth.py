import pytest
import respx

from neuroio.constants import IAM_BASE_URL


@respx.mock
def test_login_200(client_no_auth):
    request = respx.post(
        f"{IAM_BASE_URL}/v1/login/", status_code=200, content={"token": "key"}
    )
    login_response = client_no_auth.auth.login(
        username="helloworld", password="superpwd"
    )
    assert request.called
    assert login_response.status_code == 200
    assert login_response.json()["token"] == "key"


@respx.mock
@pytest.mark.asyncio
async def test_async_login_200(async_client_no_auth):
    request = respx.post(
        f"{IAM_BASE_URL}/v1/login/", status_code=200, content={"token": "key"}
    )
    login_response = await async_client_no_auth.auth.login(
        username="helloworld", password="superpwd"
    )
    assert request.called
    assert login_response.status_code == 200
    assert login_response.json()["token"] == "key"
