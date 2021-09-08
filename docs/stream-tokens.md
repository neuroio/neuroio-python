## Stream-Tokens

### Basic concepts

Stream-Tokens are used to authorize API calls from clients.

There are account, space & manager stream_tokens:

* Account stream_tokens are used to access most of the API as "default" Space
* Space stream_tokens are just restricted for using with data inside that Space
* Manager stream_tokens are restricted for using only in IAM management API

Although, there are 3 types of stream_tokens, you can use this same API for managing any of them.
Platform will know which type of token you're referring to by looking at api_token that is in your Client() instance.

You can have temporary (24 hours) or permanent token. Recommended way is to always use temporary stream_tokens inside your applications and rotate them periodically.
In order to help enforcing this practice, permanent stream_tokens are restricted to maximum 5 of them per account/space.

### Create Token

__Authorized Client() required.__

This method creates new temporary or permanent token.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.stream_tokens.create(permanent=True)
json_response = response.json()
print(json_response)
```

### List Stream-Tokens

__Authorized Client() required.__

This method returns paginated list of stream_tokens. 
Can be filtered by permanence of stream_tokens.



```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.stream_tokens.list(permanent=False, limit=10, offset=5)
json_response = response.json()  # if response is 200, this is list of dicts
print(json_response)
```

### Get Stream-Token by id

__Authorized Client() required.__

This method returns stream-token info, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.stream_tokens.get(token_id_or_key=1)
json_response = response.json()
print(json_response)
```

### Update Stream-Token by id

__Authorized Client() required.__

This method updates stream-token info, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.stream_tokens.update(token_id_or_key=1, is_active=False)
json_response = response.json()
print(json_response)
```

### Delete Token by id

__Authorized Client() required.__

This method deletes token, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
# NOTE: There is empty response in case of successful operation
response = c.stream_tokens.delete(token_id_or_key=1)
if response.status_code == 204:
    print("Stream-Token deleted successfully.")
```

### Delete List of Stream-Tokens

__Authorized Client() required.__

This method deletes many stream_tokens, if found by permanent filter.

Rules of this filter are:
* False - deletes only temporary stream_tokens
* True - deletes only permanent stream_tokens
* None - deletes all stream_tokens

```python
from neuroio import Client

c = Client(api_token="abcd")
# NOTE: There is empty response in case of successful operation
response = c.stream_tokens.delete_list(permanent=False)
if response.status_code == 204:
    print("Stream-Tokens deleted successfully.")
```