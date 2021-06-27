import os

import pytest

from homework4.task01 import is_in_interval
from homework4.task01.tests.make_temporary_test_file import make_file


@make_file(filename="happy_path.txt", content="2.1")
def test_is_in_interval_happy_path(file):
    """Happy Path is_in_interval test"""
    assert is_in_interval(file) is True


@make_file(filename="lower_border.txt", content="1\nqwerty")
def test_is_in_interval_lower_border(file):
    """Lower border + additional line is_in_interval positive test"""
    assert is_in_interval(file) is True


@make_file(filename="upper_border.txt", content="2.99")
def test_is_in_interval_upper_border(file):
    """Upper border is_in_interval positive test"""
    assert is_in_interval(file) is True


@make_file(filename="upper_border_exclusion.txt", content="3")
def test_is_in_interval_upper_border_exclusion(file):
    """Upper border is_in_interval positive test"""
    assert is_in_interval(file) is False


@make_file(filename="lower_border_positive.txt", content="0.99")
def test_is_in_interval_lower_border_outside_interval(file):
    """Lower border is_in_interval positive test"""
    assert is_in_interval(file) is False


@make_file(filename="string.txt", content="test 2. 3")
def test_is_in_interval_string(file):
    """Invalid input (string) is_in_interval"""
    with pytest.raises(ValueError):
        is_in_interval(file)


@make_file(filename="symbol.txt", content="-")
def test_is_in_interval_symbol(file):
    """Invalid input (symbol) is_in_interval negative test"""
    with pytest.raises(ValueError):
        is_in_interval(file)


@make_file(filename="empty.txt", content="")
def test_is_in_interval_empty(file):
    """Invalid input (empty) is_in_interval negative test"""
    with pytest.raises(ValueError):
        is_in_interval(file)


@make_file(filename="empty.txt", content="\n")
def test_is_in_interval_whitespace(file):
    """Invalid input (whitespace) is_in_interval negative test"""
    with pytest.raises(ValueError):
        is_in_interval(file)


def test_is_in_interval_invalid_filepath(tmp_path):
    """Invalid filepath is_in_interval negative test"""
    with pytest.raises(ValueError):
        is_in_interval(os.path.join(tmp_path, "111111111111111111.txt"))
