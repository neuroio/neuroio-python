## Utility

### Basic concepts

This section indicates those functions that are not directly related to the logic of the platform, but help in certain user scenarios.

### Compare two photos

__Authorized Client() required.__

This function compares images of faces in uploaded photos for belonging to the same person.

```python
from neuroio import Client
from neuroio.constants import EntryResult

c = Client(api_token="abcd")
with open("image1.png", "rb") as f1:
    with open("image2.png", "rb") as f2:
        response = c.utility.compare(
            image1=f1,
            image2=f2,
            result=EntryResult.HA
        )
json_response = response.json()
print(json_response)
```

### Age/Sex/Mood

__Authorized Client() required.__

This function returns age / gender / mood for the person on a given photo.

```python
from neuroio import Client

c = Client(api_token="abcd")
with open("image.png", "rb") as f:
    response = c.utility.asm(image=f)
json_response = response.json()
print(json_response)
```
