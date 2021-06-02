## Tokens

### Basic concepts

Tokens are used to authorize API calls from clients.

There are account, space & manager tokens:

* Account tokens are used to access most of the API as "default" Space
* Space tokens are just restricted for using with data inside that Space
* Manager tokens are restricted for using only in IAM management API

Although, there are 3 types of tokens, you can use this same API for managing any of them.
Platform will know which type of token you're referring to by looking at api_token that is in your Client() instance.

You can have temporary (24 hours) or permanent token. Recommended way is to always use temporary tokens inside your applications and rotate them periodically.
In order to help enforcing this practice, permanent tokens are restricted to maximum 5 of them per account/space.

### Create Token

__Authorized Client() required.__

This method creates new temporary or permanent token.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.tokens.create(permanent=True)
json_response = response.json()
print(json_response)
```

### List Tokens

__Authorized Client() required.__

This method returns paginated list of tokens. 
Can be filtered by permanence of tokens.



```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.tokens.list(permanent=False, limit=10, offset=5)
json_response = response.json()  # if response is 200, this is list of dicts
print(json_response)
```

### Get Token by id

__Authorized Client() required.__

This method returns token info, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.tokens.get(token_id_or_key=1)
json_response = response.json()
print(json_response)
```

### Update Token by id

__Authorized Client() required.__

This method updates token info, if found by its id.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.tokens.update(token_id_or_key=1, is_active=False)
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
response = c.tokens.delete(token_id_or_key=1)
if response.status_code == 204:
    print("Token deleted successfully.")
```

### Delete List of Tokens

__Authorized Client() required.__

This method deletes many tokens, if found by permanent filter.

Rules of this filter are:
* False - deletes only temporary tokens
* True - deletes only permanent tokens
* None - deletes all tokens

```python
from neuroio import Client

c = Client(api_token="abcd")
# NOTE: There is empty response in case of successful operation
response = c.tokens.delete_list(permanent=False)
if response.status_code == 204:
    print("Tokens deleted successfully.")
```