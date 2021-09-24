## Entries

### Basic concepts

Entries are containers which store the results of the processing of a photo that was uploaded to the platform. The source of the photo can be either the user (when they create or re-initialize a persona) or a surveillance camera that is connected to the platform via the preprocessing server.

When a user uploads a photo, two types of entries may appear in the platform: new and reinit. 

When video streams from network cameras are processed, all types of entries can appear in the platform: new, reinit, exact, ha, junk, nm and det.

### List Entries

__Authorized Client() required.__

This method returns paginated list of entries.

All the filtering parameters in this call are optional, this example just shows every single option.

For `sex`: 0 - male, 1 - female.

```python
import datetime

from neuroio import Client
from neuroio.constants import EntryLiveness, EntryMood, EntryResult


c = Client(api_token="abcd")
response = c.entries.list(
    pid=["abcdef01-abcd-abcd01-abcdef01"],
    result=[EntryResult.NEW],
    age_from=1,
    age_to=100,
    sex=0,
    mood=[EntryMood.FEAR],
    liveness=[EntryLiveness.PASSED],
    sources_ids=[1],
    spaces_ids=[1],
    date_from=datetime.datetime(year=2020, month=1, day=31),
    date_to=datetime.datetime.utcnow(),
    limit=10,
    offset=5
)
json_response = response.json()  # if response is 200, this is list of dicts
print(json_response)
```

### Get the statistics for a persona’s id

__Authorized Client() required.__

This method returns statistics for a person, if found by its pid.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.entries.get(pid="abcdef01-abcd-abcd01-abcdef01")
json_response = response.json()
print(json_response)
```

### Delete Entry by id

__Authorized Client() required.__

This method deletes entry, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
# NOTE: There is empty response in case of successful operation
response = c.entries.delete(id=1)
if response.status_code == 204:
    print("Entry deleted successfully.")
```
