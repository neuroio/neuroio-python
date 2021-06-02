## Who Am I

### Basic concepts

If you want to know which type of account (and info on that account) you're using, use `me` method with some token.

### Get current account info

__Authorized Client() required.__

This method gets information about current user and space (or just space, if you're using space token).

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.whoami.me()
json_response = response.json()
print(json_response)
```