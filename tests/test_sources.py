import pytest
import respx

from neuroio.constants import API_BASE_URL, EntryResult, SourceLicense


@respx.mock
def test_create_201(client):
    request = respx.post(
        f"{API_BASE_URL}/v1/sources/",
        status_code=201,
        content={"id": 1, "name": "test_name"},
    )
    response = client.sources.create(name="test_name")
    assert request.called
    assert response.status_code == 201
    assert response.json()["name"] == "test_name"


@respx.mock
def test_create_store_images_results_201(client):
    request = respx.post(
        f"{API_BASE_URL}/v1/sources/",
        status_code=201,
        content={"id": 1, "name": "test_name"},
    )
    response = client.sources.create(
        name="test_name", store_images_for_results=[EntryResult.DET]
    )
    assert request.called
    assert response.status_code == 201
    assert response.json()["name"] == "test_name"


@respx.mock
@pytest.mark.asyncio
async def test_async_create_201(async_client):
    request = respx.post(
        f"{API_BASE_URL}/v1/sources/",
        status_code=201,
        content={"id": 1, "name": "test_name"},
    )
    response = await async_client.sources.create(name="test_name")
    assert request.called
    assert response.status_code == 201
    assert response.json()["name"] == "test_name"


@respx.mock
@pytest.mark.asyncio
async def test_async_create_store_images_results_201(async_client):
    request = respx.post(
        f"{API_BASE_URL}/v1/sources/",
        status_code=201,
        content={"id": 1, "name": "test_name"},
    )
    response = await async_client.sources.create(
        name="test_name", store_images_for_results=[EntryResult.DET]
    )
    assert request.called
    assert response.status_code == 201
    assert response.json()["name"] == "test_name"


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
    response = client.sources.list(q="test", offset=20)
    assert request.called
    assert response.status_code == 200
    assert response.json()["results"][0]["name"] == "source_name"


@respx.mock
@pytest.mark.asyncio
async def test_async_list_without_params_200(async_client):
    request = respx.get(
        f"{API_BASE_URL}/v1/sources/?q=&limit=20&offset=0",
        status_code=200,
        content={"results": [{"id": 1, "name": "source_name"}]},
    )
    response = await async_client.sources.list()
    assert request.called
    assert response.status_code == 200
    assert response.json()["results"][0]["name"] == "source_name"


@respx.mock
@pytest.mark.asyncio
async def test_async_list_with_params_200(async_client):
    request = respx.get(
        f"{API_BASE_URL}/v1/sources/?q=test&limit=20&offset=20",
        status_code=200,
        content={"results": [{"id": 1, "name": "source_name"}]},
    )
    response = await async_client.sources.list(q="test", offset=20)
    assert request.called
    assert response.status_code == 200
    assert response.json()["results"][0]["name"] == "source_name"


@respx.mock
def test_retrieve_200(client):
    request = respx.get(
        f"{API_BASE_URL}/v1/sources/1/",
        status_code=200,
        content={"id": 1, "name": "source_name"},
    )
    response = client.sources.get(id=1)
    assert request.called
    assert response.status_code == 200
    assert response.json()["name"] == "source_name"


@respx.mock
def test_retrieve_404(client):
    request = respx.get(f"{API_BASE_URL}/v1/sources/1/", status_code=404)
    response = client.sources.get(id=1)
    assert request.called
    assert response.status_code == 404


@respx.mock
@pytest.mark.asyncio
async def test_async_retrieve_200(async_client):
    request = respx.get(
        f"{API_BASE_URL}/v1/sources/1/",
        status_code=200,
        content={"id": 1, "name": "source_name"},
    )
    response = await async_client.sources.get(id=1)
    assert request.called
    assert response.status_code == 200
    assert response.json()["name"] == "source_name"


@respx.mock
@pytest.mark.asyncio
async def test_async_retrieve_404(async_client):
    request = respx.get(f"{API_BASE_URL}/v1/sources/1/", status_code=404)
    response = await async_client.sources.get(id=1)
    assert request.called
    assert response.status_code == 404


@respx.mock
def test_update_200(client):
    request = respx.patch(
        f"{API_BASE_URL}/v1/sources/1/",
        status_code=200,
        content={"id": 1, "name": "source_name"},
    )
    response = client.sources.update(
        id=1, name="source_name", license_type=[SourceLicense.ADVANCED]
    )

    request_content = request.calls[0][0]
    request_content.read()

    assert request.called
    assert (
        request_content.content
        == b'{"name": "source_name", "license_type": ["advanced"]}'
    )
    assert response.status_code == 200
    assert response.json()["name"] == "source_name"


@respx.mock
@pytest.mark.asyncio
async def test_async_update_200(async_client):
    request = respx.patch(
        f"{API_BASE_URL}/v1/sources/1/",
        status_code=200,
        content={"id": 1, "name": "source_name"},
    )
    response = await async_client.sources.update(
        id=1, name="source_name", license_type=[SourceLicense.ADVANCED]
    )

    request_content = request.calls[0][0]
    request_content.read()

    assert request.called
    assert (
        request_content.content
        == b'{"name": "source_name", "license_type": ["advanced"]}'
    )
    assert response.status_code == 200
    assert response.json()["name"] == "source_name"


@respx.mock
def test_delete_202(client):
    request = respx.delete(f"{API_BASE_URL}/v1/sources/1/", status_code=202)
    response = client.sources.delete(id=1)
    assert request.called
    assert response.status_code == 202


@respx.mock
@pytest.mark.asyncio
async def test_async_delete_202(async_client):
    request = respx.delete(f"{API_BASE_URL}/v1/sources/1/", status_code=202)
    response = await async_client.sources.delete(id=1)
    assert request.called
    assert response.status_code == 202
