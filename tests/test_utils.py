from neuroio.constants import sentinel
from neuroio.utils import process_query_params, request_data_processing


def test_process_query_params():
    data = {"foo": 1, "bar": [1, 2, 3]}
    result = process_query_params(data)

    assert result == {"foo": 1, "bar": "1,2,3"}


def test_process_get_query_params():
    data = {"one": 1, "two": sentinel, "self": 3}

    result = request_data_processing(data, ["self"])
    assert result == {"one": 1}
