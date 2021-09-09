## Licenses

### Basic concepts


### Create License

__Authorized Client() required.__

This method creates new license with specified name.

All of the parameters, except `name`, are optional.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.licenses.sources.create(name="test", entry_storage_days=1)
json_response = response.json()
print(json_response)

```

### List Licenses

__Authorized Client() required.__

This method returns paginated list of licenses. 
Can be filtered by name using `q` & by list of space ids.

```python
import datetime
from neuroio import Client

c = Client(api_token="abcd")
response = c.licenses.sources.list(
    q="te",
    date_from=datetime.datetime(year=2020, month=1, day=31),
    date_to=datetime.datetime.utcnow(),
    limit=10,
    offset=5,
)
json_response = response.json()
print(json_response)

```

### Get License by id

__Authorized Client() required.__

This method returns license info, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.licenses.sources.get(id=1)
json_response = response.json()
print(json_response)
```

### Update License by id

__Authorized Client() required.__

This method updates license info, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.licenses.sources.update(
    id=1, name="test", is_active=True, entry_storage_days=3
)
json_response = response.json()
print(json_response)

```
