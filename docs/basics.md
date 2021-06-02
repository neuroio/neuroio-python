## Common usage patterns

### Basic concepts

For any call you do, in response you'll get httpx response object.
So you can do anything with it as per [httpx docs](https://www.python-httpx.org/quickstart/).
You can parse response as json, read http status code, response headers and all that good stuff.

Note that responses are only of two kinds - successes (< 400) & errors (>= 400).
Please refer to the documentation of NeuroIO API for response format in each individual case.

Unlike successful responses, errors are always the same format which can be easily parsed on client's side like so:

```python
from neuroio import Client


class NeuroIOFieldError:
    def __init__(self, name: str, message: str, error_code: int):
        self.name = name
        self.message = message
        self.error_code = error_code
        

class NeuroIOException(Exception):
    def __init__(self, json_response: dict):
        self.error_codes = json_response["error_codes"]
        self.message = json_response["message"]
        self.fields = [NeuroIOFieldError(**f) for f in json_response["fields"]]

        
if __name__ == '__main__':
    c = Client()
    response = c.spaces.create(name="test")
    if response.status_code >= 400:
        exc = NeuroIOException(json_response=response.json())
        raise exc
```
