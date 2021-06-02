## Authentication

### Basic concepts

**There are two main namespaces in NeuroIO: IAM & API.**

* IAM (identity & access management) allows you to follow authentication flow using username/password, create API access tokens for your application, manage Spaces and many more.

* API (application programming interface) allows you to interact with database of people, create sources of data, manage notifications settings and many more.

Some things to note about access tokens:

1. In order to access NeuroIO API, you need valid token. 
2. Valid token is the one, that is currently active & not expired. 
3. Tokens could be temporary & permanent (those do not expire automatically). 
4. As of now, all temporary tokens have the same TTL of 24 hours since creation time.

### Login

This method creates new temporary token for user if username/password pair is correct.

```python
from neuroio import Client

c = Client()
login_response = c.auth.login(username="usr", password="pwd")
json_login_response = login_response.json()

if login_response.status_code == 200:
    print("Login Successful.")
    print(json_login_response)
    # {
    #     'user': {
    #         'username': 'usr'
    #     },
    #     'token': {
    #         'id': 1, 
    #         'key': 'abcd', 
    #         'is_active': True, 
    #         'created': '2021-05-28T10:37:51.433760+00:00', 
    #         'expires': '2021-05-29T10:37:51.433563+00:00'
    #     }
    # }
else:
    print("Login failed.")
    print(json_login_response)
    # {
    #     'error_codes': [602], 
    #     'message': 'Username and password do not match.', 
    #     'fields': []
    # }
```

After that you need to re-create Client instance with as so:

```python
from neuroio import Client

client = Client(api_token=json_login_response["token"]["key"])

# From now on, use this new client instance whenever you access API
```

### Change password

Given correct current password, this method allows you to specify new password & optionally reset all tokens that were previously created.

```python
from neuroio import Client

c = Client(api_token="abcd")
login_response = c.auth.password_change(
    old_password="pwd",
    new_password="newpwd",
    reset_tokens=False
) 
json_response = login_response.json()

if login_response.status_code == 204:
    print("Password change successful.")
else:
    print("Password change failed.")
    print(json_response)
    # {
    #     'error_codes': [400],
    #     'message': 'Validation error.',
    #     'fields': [
    #         {
    #             'name': 'old_password',
    #             'message': 'Incorrect password.',
    #             'error_code': 400
    #         }
    #     ]
    # }

```