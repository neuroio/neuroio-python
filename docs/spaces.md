## Spaces

### Basic concepts

Spaces are a way of having multiple databases of people inside your single account.

Sources, Persons and any other entities are only visible (created & searched, for example) inside particular space you're in.

To be precise, you can't have any data in your account that isn't attached to a space. You always have space named "default", and even if you use account tokens (not space tokens), you're still using spaces (well, that "default" space).

### Create Space

__Authorized Client() required.__

This method creates new space with specified name.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.spaces.create(name="test")
json_response = response.json()
print(json_response)
```

### List Spaces

__Authorized Client() required.__

This method returns paginated list of spaces. 
Can be filtered by name using `q`.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.spaces.list(q="te", limit=10, offset=5)
json_response = response.json()
print(json_response)
```

### Get Space by id

__Authorized Client() required.__

This method returns space info, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.spaces.get(id=1)
json_response = response.json()
print(json_response)
```

### Update Space by id

__Authorized Client() required.__

This method updates space info, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.spaces.update(id=1, name="newname")
json_response = response.json()
print(json_response)
```

### Delete Space by id

__Authorized Client() required.__

This method deletes space, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
# NOTE: There is empty response in case of successful operation
response = c.spaces.delete(id=1)
if response.status_code == 204:
    print("Space deleted successfully.")
```

### Create Token for specified Space

__Authorized Client() required.__

This method creates new token for space, if found by its id.
You can create temporary or permanent token as with any other type of tokens.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.spaces.token(id=1, permanent=True)
json_response = response.json()
print(json_response)
```