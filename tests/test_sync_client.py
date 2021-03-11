from neuroio import Client


def test_client_default_api_version():
    neuroio = Client()
    assert neuroio.api_version == 1


def test_client_api_version():
    neuroio = Client(api_version=2)
    assert neuroio.api_version == 2
