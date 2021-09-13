from neuroio.constants import sentinel
from neuroio.utils import (
    process_query_params,
    request_dict_processing,
    request_form_processing,
    request_query_processing,
    validate_month_str,
)


def test_process_query_params():
    data = {"foo": 1, "bar": [1, 2, 3]}
    result = process_query_params(data)

    assert result == {"foo": 1, "bar": "1,2,3"}


def test_request_query_processing():
    data = {"one": 1, "two": sentinel, "self": 3, "three": [1, 2, 3]}

    result = request_query_processing(data)
    assert result == {"one": 1, "three": "1,2,3"}


def test_request_dict_processing_empty_exclude():
    data = {"one": 1, "two": sentinel, "self": 3, "three": [1, 2, 3]}

    result = request_dict_processing(data)
    assert result == {"one": 1, "three": [1, 2, 3]}


def test_request_dict_processing_has_exclude():
    data = {"one": 1, "two": sentinel, "self": 3, "three": [1, 2, 3]}

    result = request_dict_processing(data, ["three"])
    assert result == {"one": 1}


def test_request_form_processing_empty_exclude():
    data = {"one": 1, "two": sentinel, "self": 3, "three": "3"}

    result = request_form_processing(data)
    assert result == {"one": "1", "three": "3"}


def test_request_form_processing_has_exclude():
    data = {"one": 1, "two": sentinel, "self": 3, "three": "3"}

    result = request_form_processing(data, ["three"])
    assert result == {"one": "1"}


def test_validate_month_str():
    month_str = "2018*09"
    in_assertion = False
    try:
        validate_month_str(month_str)
    except ValueError:
        in_assertion = True
    assert in_assertion
