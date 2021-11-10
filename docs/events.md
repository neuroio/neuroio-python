## WebSocket Events Listener

### Basic concepts

Included class EventListener is used to asynchronously listen to events coming over WebSocket connection via wss://events.neuroio.com

Reference for communication protocol & objects structure can be found here: https://kb.neuroio.com/#/notifications?id=creating-a-connection-to-the-platform-with-websocket 

There are only 4 types of messages as of now:

1) Response for AUTH message
2) Response for PING message
3) Error messages
4) Event data message

We highly recommend using `uvloop` library for better performance in high-load usage scenarios.

This is a basic but sufficient example of how to use EventListener and receive events in your application:

```python
import asyncio
import json
import logging
import signal

from neuroio import EventListener


async def event_handler_func(event_message: str):
    # NOTE: this must be awaitable and accept single param Union[str, bytes]
    json_message = json.loads(event_message)
    is_ping_response = "PING" in json_message.keys()
    is_auth_response = "auth" in json_message.keys()
    is_error_response = "error" in json_message.keys()
    if is_ping_response:
        if json_message["PING"] != "PONG":
            # something is wrong with socket connection
            raise RuntimeError()
        else:
            # this is correct pong response on our periodic pings
            logging.info("Connection is alive")
    elif is_auth_response:
        logging.info("Authorized successfully")
    elif is_error_response:
        # something is wrong with provided token
        logging.info(json_message["error"], flush=True)
    else:
        # this must be event about entry itself
        # now you can inspect json_message for information about that
        logging.info(json_message["data"]["face_image"])


async def shutdown(signal, loop):
    """Cleanup tasks tied to the service's shutdown."""
    logging.info(f"Received exit signal {signal.name}...")
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]

    [task.cancel() for task in tasks]

    logging.info(f"Cancelling {len(tasks)} outstanding tasks")
    await asyncio.gather(*tasks, return_exceptions=True)
    loop.stop()


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    
    # NOTE: You are advised to hook-up uvloop here for improved performance
    
    api_token = "1234567890"
    events_listener = EventListener(
        api_token=api_token, event_handler_func=event_handler_func
    )

    loop = asyncio.get_event_loop()
    # May want to catch other signals too
    signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT)
    for s in signals:
        loop.add_signal_handler(
            s, lambda _s=s: asyncio.create_task(shutdown(_s, loop))
        )

    try:
        loop.create_task(events_listener.listen())
        loop.run_forever()
    finally:
        loop.close()
        logging.info("Successfully shutdown")

```