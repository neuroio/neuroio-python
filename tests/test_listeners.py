import asyncio
import functools
import json

import pytest

from neuroio import EventListener


@pytest.mark.asyncio
async def test_listener_has_entry_events_and_auth_and_ping():
    received_msgs = []

    async def event_handler_func(_received_msgs, message: str) -> None:
        _received_msgs.append(message)

    api_token = "1234567890"
    events_listener = EventListener(
        api_token=api_token,
        event_handler_func=functools.partial(
            event_handler_func, received_msgs
        ),
    )
    task = asyncio.create_task(events_listener.listen())
    await asyncio.sleep(3)
    task.cancel()
    json_received_msgs = list(map(lambda x: json.loads(x), received_msgs))
    assert {"auth": "ok"} in json_received_msgs
    assert {"PING": "PONG"} in json_received_msgs
    assert {"id": 1, "data": {"result": "new"}} in json_received_msgs


@pytest.mark.asyncio
async def test_listener_bytes_received():
    received_msgs = []

    async def event_handler_func(_received_msgs, message: str) -> None:
        _received_msgs.append(message)

    api_token = "bytes"
    events_listener = EventListener(
        api_token=api_token,
        event_handler_func=functools.partial(
            event_handler_func, received_msgs
        ),
    )
    task = asyncio.create_task(events_listener.listen())
    await asyncio.sleep(3)
    task.cancel()
    json_received_msgs = list(map(lambda x: json.loads(x), received_msgs))
    assert [{"auth": "ok"}, {"PING": "PONG"}] == json_received_msgs


@pytest.mark.asyncio
async def test_listener_server_closed_connection():
    received_msgs = []

    async def event_handler_func(_received_msgs, message: str) -> None:
        _received_msgs.append(message)

    api_token = "close"
    events_listener = EventListener(
        api_token=api_token,
        event_handler_func=functools.partial(
            event_handler_func, received_msgs
        ),
    )
    task = asyncio.create_task(events_listener.listen())
    await asyncio.sleep(3)
    task.cancel()
    json_received_msgs = list(map(lambda x: json.loads(x), received_msgs))
    assert {"auth": "ok"} in json_received_msgs
    assert {"PING": "PONG"} not in json_received_msgs
    assert {"id": 1, "data": {"result": "new"}} not in json_received_msgs


@pytest.mark.asyncio
async def test_listener_server_closed_unexpectedly_connection():
    received_msgs = []

    async def event_handler_func(_received_msgs, message: str) -> None:
        _received_msgs.append(message)

    api_token = "close_102"
    events_listener = EventListener(
        api_token=api_token,
        event_handler_func=functools.partial(
            event_handler_func, received_msgs
        ),
    )
    task = asyncio.create_task(events_listener.listen())
    await asyncio.sleep(3)
    task.cancel()
    json_received_msgs = list(map(lambda x: json.loads(x), received_msgs))
    assert {"auth": "ok"} in json_received_msgs
    assert {"PING": "PONG"} not in json_received_msgs
    assert {"id": 1, "data": {"result": "new"}} not in json_received_msgs
