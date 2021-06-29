from unittest.mock import patch

import pytest
import requests

from homework4.task02 import count_dots_on_i


class FakeResponse:
    """A class that contains response content for tests"""

    def __init__(self, value="default"):
        self.text = value


def test_count_dots_on_i_happy_path():
    """Happy path count_dots_on_i test"""
    with patch("requests.get") as mock_request:
        response_text = (
            "Lorem ipsum dolor sit amet, 123 consectetur adipiscing elit@#$%^&*()_+. Nullam I sit amet "
            "accumsan purus. "
        )
        mock_request.return_value = FakeResponse(response_text)
        count = count_dots_on_i("https://example.com/")
        assert count == 7


def test_count_dots_on_i_no_i():
    """count_dots_on_i test: no 'i' characters in response"""
    with patch("requests.get") as mock_request:
        response_text = "test"
        mock_request.return_value = FakeResponse(response_text)
        count = count_dots_on_i("https://example.com/")
        assert count == 0


def test_count_dots_on_i_error_handling():
    """count_dots_on_i test: RequestException handling"""
    with patch("requests.get") as mock_request:
        with pytest.raises(ValueError):
            mock_request.side_effect = requests.exceptions.RequestException
            count_dots_on_i("https://example.com/")
