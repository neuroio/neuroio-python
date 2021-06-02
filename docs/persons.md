## Persons

### Basic concepts

Persons are wrapped face embeddings that come through user uploads or automatically from connected cameras. 
In fact, this is the similar "tag" as sources, but if the sources indicate where the photo came from, 
then the person is a tag indicating who is on it.

Entry types that are always associated with persons: new, reinit, exact, ha, junk. 
The types of records nm, det cannot be associated with persons, 
since in this case the platform does not know who is in the photo.

Any work with persons implies the automatic scope of the token with which the request is made. 
When created, created from id, upon reinit, Entries and Persons fall into the same space
where the source specified in the request is located 
(again, provided that this source is visible from the current token space).

### Create Person

__Authorized Client() required.__

This method creates (or finds, to avoid duplicates) person using provided photo.

```python
from neuroio import Client

c = Client(api_token="abcd")
with open("image.png", "rb") as f:
    response = c.persons.create(
        image=f,
        source="test",
        facesize=1000,
        create_on_ha=True,
        create_on_junk=False,
        identify_asm=True
    )
json_response = response.json()
print(json_response)
```

### Create Person from Entry

__Authorized Client() required.__

This method creates new persons from photo on specified Entry ID.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.persons.create_by_entry(
    id=1, 
    create_on_ha=False, 
    create_on_junk=False
)
json_response = response.json()
print(json_response)
```

### Re-init Person from photo in specified Entry ID. 

__Authorized Client() required.__

This method changes face embedding for a specified persons to the one, extracted from photo in Entry.

```python
from neuroio import Client

c = Client(api_token="abcd")
response = c.persons.reinit(id=1)
# NOTE: There is empty response in case of successful operation
```

### Re-init Person from provided photo 

__Authorized Client() required.__

This method changes face embedding for a specified persons to the one, extracted from provided photo.

```python
from neuroio import Client
from neuroio.constants import EntryResult

c = Client(api_token="abcd")
with open("image.png", "rb") as f:
    response = c.persons.reinit_by_photo(
        pid="abcdef01-abcd-abcd01-abcdef01",
        image=f,
        source="test",
        facesize=1000,
        identify_asm=True,
        result=EntryResult.HA,
    )
# NOTE: There is empty response in case of successful operation
```

### Search Person by provided photo

__Authorized Client() required.__

This method searches for a person in database, comparing face embedding from provided photo.

```python
from neuroio import Client

c = Client(api_token="abcd")
with open("image.png", "rb") as f:
    response = c.persons.search(image=f, identify_asm=True)

json_response = response.json()
print(json_response)
```

### Delete Person by PID

__Authorized Client() required.__

This method deletes person, if found by its pid.

```python
from neuroio import Client

c = Client(api_token="abcd")
# NOTE: There is empty response in case of successful operation
response = c.persons.delete(pid="abcdef01-abcd-abcd01-abcdef01")
if response.status_code == 204:
    print("Person deleted successfully.")
```