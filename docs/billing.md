## Billing

### Basic concepts

Billing module provides methods to get insight about user's usage of platform resources. 

You can filter billing data by month, spaces, and types of events.

Event types options are:

    API_CALLS = 1
    PERSONS_STORAGE = 2
    ENTRY_STORAGE = 3
    SOURCE_LICENSES = 4

### Billing Usage

__Authorized Client() required.__

This method returns paginated list of billing usage. Available only for users and spaces.
Available only for access tokens.
Can be filtered by name using list of event types & by list of space ids and months range.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.billing.usage(
    month_from="2020-01",
    month_to="2020-06",
    spaces_ids=[4, 5, 6],
    event_types=[1, 2, 3],
    limit=10,
    offset=5,
)
json_response = response.json()
print(json_response)
```

### Billing Total Usage

__Authorized Client() required.__

This method returns billing usage. 
Available only for users and spaces.
Available only for access tokens.
Can be filtered by name using list of event types and months range.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.billing.usage_total(
    month_from="2020-01", 
    month_to="2020-06", 
    event_types=[1, 2, 3],
    spaces_ids=[4, 5, 6],
)
json_response = response.json()
print(json_response)
```
