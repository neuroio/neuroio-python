# from neuroio import Client
# from neuroio.utils import get_package_version
#
#
# def test_client_default_api_version():
#     neuroio = Client()
#     assert neuroio.api_version == 1
#
#
# def test_client_api_version():
#     neuroio = Client(api_version=2)
#     assert neuroio.api_version == 2
#
#
# def test_client_no_api_token_client_without_auth():
#     neuroio = Client()
#     assert not neuroio.api_token
#     assert neuroio.api_client.auth is None
#     assert neuroio.iam_client.auth is None
#
#
# def test_client_api_token_sets_auth():
#     rnd_str = "helloworld"
#     neuroio = Client(api_token=rnd_str)
#     assert neuroio.api_token == rnd_str
#     assert neuroio.iam_client.auth is not None
#
#
# def test_client_set_api_token_after_instance_is_created():
#     rnd_str = "helloworld"
#     neuroio = Client()
#     neuroio.inject_api_token(rnd_str)
#     assert neuroio.api_token == rnd_str
#     assert neuroio.api_client.auth is not None
#     assert neuroio.iam_client.auth is not None
#
#
# def test_client_has_version_in_user_agent_header():
#     neuroio = Client(api_token="helloworld")
#     assert get_package_version() in neuroio.api_client.headers["User-Agent"]
#     assert get_package_version() in neuroio.iam_client.headers["User-Agent"]
