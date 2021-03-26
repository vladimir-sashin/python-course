from unittest.mock import mock_open, patch

from homework1.task03 import find_maximum_and_minimum


def test_min_max_integers():
    with patch("builtins.open", mock_open(read_data="557\n0\n-835\n4\n174\n-6\n978")):
        assert find_maximum_and_minimum("path") == (-835, 978)


def test_min_max_one_line():
    with patch("builtins.open", mock_open(read_data="3")):
        assert find_maximum_and_minimum("path") == (3, 3)
