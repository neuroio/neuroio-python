## Sources

### Basic concepts

A source in the platform is a tag for the correct cataloging and correlation of incoming data, as well as a container with user settings which indicate how this data should be processed.

All data stored in the platform must have as one of its attributes the name of its source, because only then can the platform accurately identify where the data has come from into the platform, and, as a result, correctly catalog it and execute custom logic.

Before you begin uploading data to the platform, make sure to create a source with the same name that you will then specify in your API request or when connecting a camera to the preprocessing server.

All data that is intended for cataloging and storage in the platform cannot be saved in the platform if when it is uploaded no source is specified or a source that does not exist is specified. An error message will appear each time this happens.

### Create Source

__Authorized Client() required.__

This method creates new source with specified name.

All of the parameters, except `name`, are optional.

```python
from neuroio import Client
from neuroio.constants import EntryResult

c = Client(api_token="abcd")
response = c.sources.create(
    name="test",
    license=1,
    identify_facesize_threshold=1000,
    use_pps_time=True,
    manual_create_facesize_threshold=1000,
    manual_create_on_ha=True,
    manual_create_on_junk=True,
    manual_identify_asm=False,
    auto_create_persons=True,
    auto_create_facesize_threshold=1000,
    auto_create_check_blur=True,
    auto_create_check_exposure=True,
    auto_create_on_ha=False,
    auto_create_on_junk=False,
    auto_check_face_angle=False,
    auto_check_liveness=False,
    auto_create_liveness_only=False,
    auto_identify_asm=False,
    store_images_for_results=[EntryResult.DET]
)
json_response = response.json()
print(json_response)
```

### List Sources

__Authorized Client() required.__

This method returns paginated list of sources. 
Can be filtered by name using `q` & by list of space ids.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.sources.list(q="te", spaces_ids=[1, 2], limit=10, offset=5)
json_response = response.json()
print(json_response)
```

### Get Source by id

__Authorized Client() required.__

This method returns source info, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.sources.get(id=1)
json_response = response.json()
print(json_response)
```

### Update Source by id

__Authorized Client() required.__

This method updates source info, if found by its id.

```python
from neuroio import Client
from neuroio.constants import EntryResult

c = Client(api_token="abcd")
response = c.sources.update(
    id=1, 
    name="test",
    license=1,
    identify_facesize_threshold=1000,
    use_pps_time=True,
    manual_create_facesize_threshold=1000,
    manual_create_on_ha=True,
    manual_create_on_junk=True,
    manual_identify_asm=False,
    auto_create_persons=True,
    auto_create_facesize_threshold=1000,
    auto_create_check_blur=True,
    auto_create_check_exposure=True,
    auto_create_on_ha=False,
    auto_create_on_junk=False,
    auto_check_face_angle=False,
    auto_check_liveness=False,
    auto_create_liveness_only=False,
    auto_identify_asm=False,
    store_images_for_results=[EntryResult.DET]
)
json_response = response.json()
print(json_response)
```

### Delete Source by id

__Authorized Client() required.__

This method deletes source, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
# NOTE: There is empty response in case of successful operation
response = c.sources.delete(id=1)
if response.status_code == 202:
    print("Source deleted successfully.")
```
