import pytest

from homework9.task2 import Suppressor, suppressor


def test_suppressor_class():
    with Suppressor(IndexError):
        [][2]


def test_suppressor_function():
    with suppressor(IndexError):
        [][2]


def test_suppressor_class_doesnt_suppress_other_exceptions():
    with pytest.raises(AttributeError):
        with Suppressor(IndexError):
            [].qwe


def test_suppressor_function_doesnt_suppress_other_exceptions():
    with pytest.raises(AttributeError):
        with suppressor(IndexError):
            [].qwe
