## Notifications

### Basic concepts

The notification service allows you to receive filtered data about events as soon as they happened, and without the need to constantly query the platform.

The platform supports the following types of transport:

* webhook - when an event occurs, a POST or GET request with a fixed syntax is sent to the specified url;
* websocket - the client application itself initiates a connection to the service and receives a notification on it in the format of websocket messages.

For applications in which the speed of informing about events that have occurred in the platform is important, it is recommended to use a websocket connection. This type of transport is always on, no pre-filtering is provided.

For client applications operating in gray networks and receiving data directly from the platform, only websocket transport is suitable for use.

Folliwing sections only apply to webhooks!

### Create Notification

__Authorized Client() required.__

This method creates new notification with specified parameters.

```python
from neuroio import Client
from neuroio.constants import (
    EntryLiveness,
    EntryMood,
    EntryResult,
    HttpMethod,
    Sex,
)

c = Client(api_token="abcd")
response = c.notifications.create(
    name="test",
    http_method=HttpMethod.POST,
    destination_url="https://neuroio.com/",
    is_active=True,
    moods=[EntryMood.FEAR],
    results=[EntryResult.NEW],
    liveness=[EntryLiveness.PASSED],
    age_from=1,
    age_to=100,
    sex=Sex.MALE,
    sources=[1, 2, 3],
    persons_groups=[4, 5, 6],
)
json_response = response.json()
print(json_response)
```

### List Notifications

__Authorized Client() required.__

This method returns paginated list of notifications. 
Can be filtered by name using `q`, also, by list of Spaces IDs.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.notifications.list(
    q="te",
    spaces_ids=[1, 2],
    limit=10, 
    offset=5
)
json_response = response.json()
print(json_response)
```

### Get Notification by id

__Authorized Client() required.__

This method returns notification info, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.notifications.get(id=1)
json_response = response.json()
print(json_response)
```

### Update Notification by id

__Authorized Client() required.__

This method updates notification info, if found by its id.

```python
from neuroio import Client
from neuroio.constants import (
    EntryLiveness,
    EntryMood,
    EntryResult,
    HttpMethod,
    Sex,
)

c = Client(api_token="abcd")
response = c.notifications.update(
    name="test",
    http_method=HttpMethod.POST,
    destination_url="https://neuroio.com/",
    is_active=True,
    moods=[EntryMood.FEAR],
    results=[EntryResult.NEW],
    liveness=[EntryLiveness.PASSED],
    age_from=1,
    age_to=100,
    sex=Sex.MALE,
    sources=[1, 2, 3],
    persons_groups=[4, 5, 6],
)
json_response = response.json()
print(json_response)
```

### Delete Notification by id

__Authorized Client() required.__

This method deletes notification, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
# NOTE: There is empty response in case of successful operation
response = c.notifications.delete(id=1)
if response.status_code == 204:
    print("Notification deleted successfully.")
```
