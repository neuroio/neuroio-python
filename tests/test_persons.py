import pytest
import respx

from neuroio.constants import API_BASE_URL, EntryResult


@respx.mock
def test_create_201(client):
    request = respx.post(
        f"{API_BASE_URL}/v1/persons/",
        status_code=201,
        content={"result": "new", "confidence": 100},
    )
    response = client.persons.create(
        b"image", "test_source", 1000, True, True, True
    )

    assert request.called
    assert response.status_code == 201


@respx.mock
def test_create_400(client):
    request = respx.post(f"{API_BASE_URL}/v1/persons/", status_code=400)
    response = client.persons.create(
        b"image", "test_source", 1000, True, True, True
    )

    assert request.called
    assert response.status_code == 400


@respx.mock
@pytest.mark.asyncio
async def test_async_create_200(async_client):
    request = respx.post(
        f"{API_BASE_URL}/v1/persons/",
        status_code=201,
        content={"result": "new", "confidence": 100},
    )
    response = await async_client.persons.create(
        b"image", "test_source", 1000, True, True, True
    )

    assert request.called
    assert response.status_code == 201


@respx.mock
@pytest.mark.asyncio
async def test_async_create_400(async_client):
    request = respx.post(f"{API_BASE_URL}/v1/persons/", status_code=400)
    response = await async_client.persons.create(
        b"image", "test_source", 1000, True, True, True
    )

    assert request.called
    assert response.status_code == 400


@respx.mock
def test_create_by_entry_201(client):
    request = respx.post(f"{API_BASE_URL}/v1/persons/entry/", status_code=201)
    response = client.persons.create_by_entry(1, False, False)

    assert request.called
    assert response.status_code == 201


@respx.mock
@pytest.mark.asyncio
async def test_async_create_by_entry_201(async_client):
    request = respx.post(f"{API_BASE_URL}/v1/persons/entry/", status_code=201)
    response = await async_client.persons.create_by_entry(1, False, False)
    assert request.called
    assert response.status_code == 201


@respx.mock
def test_reinit_204(client):
    request = respx.post(f"{API_BASE_URL}/v1/persons/reinit/", status_code=204)
    response = client.persons.reinit(1)
    assert request.called
    assert response.status_code == 204


@respx.mock
@pytest.mark.asyncio
async def test_async_204(async_client):
    request = respx.post(f"{API_BASE_URL}/v1/persons/reinit/", status_code=204)
    response = await async_client.persons.reinit(1)
    assert request.called
    assert response.status_code == 204


@respx.mock
def test_delete(client):
    request = respx.delete(f"{API_BASE_URL}/v1/persons/pid/", status_code=204)
    response = client.persons.delete("pid")

    assert request.called
    assert response.status_code == 204


@respx.mock
@pytest.mark.asyncio
async def test_async_delete(async_client):
    request = respx.delete(f"{API_BASE_URL}/v1/persons/pid/", status_code=204)
    response = await async_client.persons.delete("pid")

    assert request.called
    assert response.status_code == 204


@respx.mock
def test_reinit_by_photo_204(client):
    request = respx.post(
        f"{API_BASE_URL}/v1/persons/reinit/pid/", status_code=204
    )
    response = client.persons.reinit_by_photo(
        "pid", b"image", "source_name", 100, True
    )
    assert request.called
    assert response.status_code == 204


@respx.mock
def test_reinit_by_photo_400(client):
    request = respx.post(
        f"{API_BASE_URL}/v1/persons/reinit/pid/", status_code=400
    )
    response = client.persons.reinit_by_photo(
        "pid", b"image", "source_name", 100, True
    )
    assert request.called
    assert response.status_code == 400


@respx.mock
@pytest.mark.asyncio
async def test_async_reinit_by_photo_204(async_client):
    request = respx.post(
        f"{API_BASE_URL}/v1/persons/reinit/pid/", status_code=204
    )
    response = await async_client.persons.reinit_by_photo(
        "pid", b"image", "source_name", 100, True
    )

    assert request.called
    assert response.status_code == 204


@respx.mock
@pytest.mark.asyncio
async def test_async_reinit_by_photo_400(async_client):
    request = respx.post(
        f"{API_BASE_URL}/v1/persons/reinit/pid/", status_code=400
    )
    response = await async_client.persons.reinit_by_photo(
        "pid", b"image", "source_name", 100, True
    )

    assert request.called
    assert response.status_code == 400


@respx.mock
def test_search_200(client):
    request = respx.post(
        f"{API_BASE_URL}/v1/persons/search/",
        status_code=200,
        content={"result": EntryResult.NEW, "pid": "pid"},
    )
    response = client.persons.search(b"photo")
    assert request.called
    assert response.status_code == 200
    assert response.json()["pid"] == "pid"


@respx.mock
def test_search_not_found_200(client):
    request = respx.post(f"{API_BASE_URL}/v1/persons/search/", status_code=200)
    response = client.persons.search(b"photo")
    assert request.called
    assert response.status_code == 200


@respx.mock
@pytest.mark.asyncio
async def test_async_search_200(async_client):
    request = respx.post(
        f"{API_BASE_URL}/v1/persons/search/",
        status_code=200,
        content={"result": EntryResult.NEW, "pid": "pid"},
    )
    response = await async_client.persons.search(b"photo")
    assert request.called
    assert response.status_code == 200
    assert response.json()["pid"] == "pid"


@respx.mock
@pytest.mark.asyncio
async def test_async_not_found_200(async_client):
    request = respx.post(f"{API_BASE_URL}/v1/persons/search/", status_code=200)
    response = await async_client.persons.search(b"image")
    assert request.called
    assert response.status_code == 200
