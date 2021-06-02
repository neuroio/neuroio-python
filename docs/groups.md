## Person Groups

### Basic concepts

You can group persons into arbitrary lists. 
If the identified person is included in any group or groups, 
then notifications from the platform will contain not only the person's identifier, 
but also the names of all groups in which user is included.

Each person can be added to any number of groups.

Each group can contain a maximum of 100,000 persons.

### Create Person Group

__Authorized Client() required.__

This method creates new person group.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.groups.create(name="test")
json_response = response.json()
print(json_response)
```

### List Person Groups

__Authorized Client() required.__

This method returns paginated list of groups. 

Can be filtered by name using `q`.

All the filtering parameters in this call are optional, this example just shows every single option.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.groups.list(
    q="te",
    pids_include=["abcdef01-abcd-abcd01-abcdef01"],
    pids_exclude=["fedcab10-dcba-dcba10-fedcab10"],
    groups_ids=[1, 2, 3],
    spaces_ids=[4, 5, 6],
    limit=10, 
    offset=5
)
json_response = response.json()
print(json_response)
```

### Get Person Group by id

__Authorized Client() required.__

This method returns group info, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.groups.get(id=1)
json_response = response.json()
print(json_response)
```

### Update Person Group by id

__Authorized Client() required.__

This method updates group info, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.groups.update(id=1, name="newname")
json_response = response.json()
print(json_response)
```

### Delete Person Group by id

__Authorized Client() required.__

This method deletes group, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
# NOTE: There is empty response in case of successful operation
response = c.groups.delete(id=1)
if response.status_code == 204:
    print("Person Group deleted successfully.")
```

### Get a list of persons in a group

__Authorized Client() required.__

This method returns paginated results of persons that are in a group, if found by id.

You can filter out list by specifying exact list of PIDs.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.groups.persons(
    id=1,
    pids=["abcdef01-abcd-abcd01-abcdef01"],
    limit=5,
    offset=0
)
json_response = response.json()
print(json_response)
```

### Add persons to groups

__Authorized Client() required.__

This method allows you to add many persons to many groups in one request.

Max PIDs in request - 100.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.groups.add(
    pids=["abcdef01-abcd-abcd01-abcdef01"],
    groups_ids=[1, 2, 3, 4, 5]
)
```

### Remove persons to groups

__Authorized Client() required.__

This method allows you to remove many persons from many groups in one request.

Max PIDs in request - 100.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.groups.remove(
    pids=["abcdef01-abcd-abcd01-abcdef01"],
    groups_ids=[1, 2, 3, 4, 5]
)
```
