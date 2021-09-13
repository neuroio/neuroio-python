import os

from neuroio.constants import sentinel
from neuroio.utils import (
    prepare_image_processing,
    process_query_params,
    request_dict_processing,
    request_form_processing,
    request_query_processing,
)


def test_prepare_image_processing_binary():
    data = b"test_image_data"
    image = prepare_image_processing(data)

    assert isinstance(image, dict)
    assert "image" in image
    assert isinstance(image["image"], tuple)
    assert len(image["image"]) == 3
    assert image["image"][1] is not None
    assert image["image"][1].read() == data


def test_prepare_image_processing_buffer_reader():
    filename = "image.jpg"
    data = b"test_image_data"

    with open(filename, "wb") as f:
        f.write(data)

    with open(filename, "rb") as f:
        image = prepare_image_processing(f)

        assert isinstance(image, dict)
        assert "image" in image
        assert isinstance(image["image"], tuple)
        assert len(image["image"]) == 3
        assert image["image"][1] is not None

        image_data = image["image"][1].read()

    os.remove(filename)

    assert image_data == data


def test_prepare_image_processing_tuple():
    filename = "image.jpg"
    data = b"test_image_data"

    with open(filename, "wb") as f:
        f.write(data)

    with open(filename, "rb") as f:
        image = prepare_image_processing((filename, f))

        assert isinstance(image, dict)
        assert "image" in image
        assert isinstance(image["image"], tuple)
        assert len(image["image"]) == 3
        assert image["image"][1] is not None

        image_data = image["image"][1].read()

    os.remove(filename)

    assert image_data == data


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
