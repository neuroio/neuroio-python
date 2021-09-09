import os

import _io

from neuroio.constants import sentinel
from neuroio.utils import (
    prepare_image_processing,
    process_query_params,
    request_dict_processing,
    request_form_processing,
    request_query_processing,
)


def test_prepare_image_processing_binary():
    data = b"testdata"
    name, image_data = prepare_image_processing(data)

    assert isinstance(image_data, _io.BytesIO)
    assert image_data.read() == data


def test_prepare_image_processing_buffer_reader():
    filename = "image.jpg"
    data = b"test_image_data"

    with open(filename, "wb") as f:
        f.write(data)

    with open(filename, "rb") as f:
        result = prepare_image_processing(f).read()

    os.remove(filename)

    assert result == data


def test_prepare_image_processing_tuple():
    filename = "image.jpg"
    data = b"test_image_data"

    with open(filename, "wb") as f:
        f.write(data)

    with open(filename, "rb") as f:
        result = prepare_image_processing((filename, f))[1].read()

    os.remove(filename)

    assert result == data


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
