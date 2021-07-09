import pytest

from homework8.task1 import KeyValueStorage
from homework8.task1.tests.make_temporary_test_file import make_file


@make_file("name=kek\nlast_name=top")
def test_read_no_numbers(file):
    """Read file that doesn't contain any numbers (both keys and values)"""
    storage = KeyValueStorage(file)
    assert (storage.last_name, storage["last_name"]) == ("top", "top")


@make_file("name=kek\n2.5=top")
def test_read_float_key(file):
    """Read file that contains float number as a key"""
    with pytest.raises(ValueError):
        KeyValueStorage(file)


@make_file("name=kek\n-2.5=top")
def test_read_negative_float_key(file):
    """Read file that contains negative float number as a key"""
    with pytest.raises(ValueError):
        KeyValueStorage(file)


@make_file("name=kek\n5=top")
def test_read_int_key(file):
    """Read file that contains integer number as a key"""
    with pytest.raises(ValueError):
        KeyValueStorage(file)


@make_file("name=kek\n-5=top")
def test_read_negative_int_key(file):
    """Read file that contains negative integer number as a key"""
    with pytest.raises(ValueError):
        KeyValueStorage(file)


@make_file("name=kek\nlast_name=123")
def test_read_int_value(file):
    """Read file that contains integer number as a value"""
    storage = KeyValueStorage(file)
    assert (storage.last_name, storage["last_name"]) == (123, 123)


@make_file("name=kek\nlast_name=-123")
def test_read_negative_int_value(file):
    """Read file that contains integer number as a value"""
    storage = KeyValueStorage(file)
    assert (storage.last_name, storage["last_name"]) == (-123, -123)


@make_file("name=kek\nlast_name=123.5")
def test_read_float_value(file):
    """Read file that contains float number as a value"""
    storage = KeyValueStorage(file)
    assert (storage.last_name, storage["last_name"]) == (123.5, 123.5)


@make_file("name=kek\nlast_name=-123.5")
def test_read_negative_float_value(file):
    """Read file that contains float number as a value"""
    storage = KeyValueStorage(file)
    assert (storage.last_name, storage["last_name"]) == (-123.5, -123.5)


@make_file("name=kek\n_pairs=top")
def test_key_and_attribute_name_conflict(file):
    """Read file that contains a key that == existing KeyValueStorage object attribute,
    and try to get it's value by '.key'"""
    storage = KeyValueStorage(file)
    assert storage._pairs != "top"


@make_file("name=kek\n_pairs=top")
def test_key_and_attribute_name_conflict_get_value_by_brackets(file):
    """Read file that contains a key that == existing KeyValueStorage object attribute,
    and get it's value by '[key]'"""
    storage = KeyValueStorage(file)
    assert storage["_pairs"] == "top"
