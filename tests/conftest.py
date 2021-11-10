import asyncio
import json
import logging

import pytest
import websockets

from neuroio import AsyncClient, Client, constants


@pytest.fixture(scope="session")
def monkeypatch_scope_session():
    """
    This is defined for ability of session-scoped fixtures to use monkeypatch.
    """
    from _pytest.monkeypatch import MonkeyPatch

    mpatch = MonkeyPatch()
    yield mpatch
    mpatch.undo()


@pytest.fixture(scope="session")
def event_loop():
    """
    Run coroutines in non async code
    by using a new event_loop

    See: https://github.com/pytest-dev/pytest-asyncio/issues/93
    """
    old_loop = asyncio.get_event_loop()
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    try:
        yield new_loop
    finally:
        asyncio.set_event_loop(old_loop)


@pytest.fixture
def client_no_auth():
    return Client()


@pytest.fixture
async def async_client_no_auth():
    return AsyncClient()


@pytest.fixture
def client():
    return Client(api_token="token")


@pytest.fixture
async def async_client():
    return AsyncClient(api_token="token")


@pytest.fixture(scope="session", autouse=True)
def patch_events_base_url():
    base_value = constants.EVENTS_BASE_URL
    constants.EVENTS_BASE_URL = "ws://localhost:63636/"
    yield
    constants.EVENTS_BASE_URL = base_value


@pytest.fixture(scope="session", autouse=True)
async def ws_server():
    async def handler(websocket, path):
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "PING":
                await websocket.send(json.dumps({"PING": "PONG"}))
            elif data["action"] == "AUTH":
                await websocket.send(json.dumps({"auth": "ok"}))
                token = data["data"]["token"]
                if token == "close":
                    await websocket.close()
                elif token == "close_102":
                    await websocket.close(code=102, reason="test")
                elif token == "bytes":
                    await websocket.send(b"test")
                else:
                    await websocket.send(
                        json.dumps({"id": 1, "data": {"result": "new"}})
                    )
            else:
                logging.error("unsupported event: %s", data)

    async def server():
        async with websockets.serve(handler, "localhost", 63636):
            await asyncio.Future()  # run forever

    task = asyncio.create_task(server())
    yield
    task.cancel()
