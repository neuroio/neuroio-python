## Threshold Settings

### Basic concepts

The platform operates with events that have several types of results. 
The results have predefined thresholds, but the threshold values can be changed if necessary using settings.

New threshold values will be applied only for the classification of future Entries, the classification of previous Entries cannot be changed.

You can have different threshold settings for different spaces (very useful in some security scenarios).

### Get current thresholds

__Authorized Client() required.__

This method get the info about current threshold settings.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.settings.get()
json_response = response.json()
print(json_response)
```

### Update threshold settings

__Authorized Client() required.__

This method updates the values of threshold settings.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.settings.update(
    exact=90.0,
    ha=80.0,
    junk=70.0,
)
json_response = response.json()
print(json_response)
```

### Reset current thresholds to defaults

__Authorized Client() required.__

This method sets all threshold settings to default ones.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.settings.reset()
json_response = response.json()
print(json_response)
```