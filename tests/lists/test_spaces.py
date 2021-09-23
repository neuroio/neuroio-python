import pytest
import respx

from neuroio.constants import IAM_BASE_URL


@respx.mock
def test_spaces_full_list(client):
    request = respx.get(f"{IAM_BASE_URL}/v1/lists/spaces/").respond(
        status_code=200
    )
    response = client.lists.spaces.all()
    assert request.called
    assert response.status_code == 200


@respx.mock
@pytest.mark.asyncio
async def test_async_spaces_full_list(async_client):
    request = respx.get(f"{IAM_BASE_URL}/v1/lists/spaces/").respond(
        status_code=200
    )
    response = await async_client.lists.spaces.all()

    assert request.called
    assert response.status_code == 200
