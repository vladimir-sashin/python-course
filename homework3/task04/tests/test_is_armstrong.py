import pytest

from homework3.task04 import better_is_armstrong, is_armstrong

test_data_single_digits = [(0, True), (1, True), (3, True), (9, True)]

test_data_true = [(153, True), (370, True), (371, True), (548834, True)]

test_data_false = [(10, False), (11, False), (55, False), (154, False), (777, False)]

# tests for is_armstrong


@pytest.mark.parametrize("test_input,expected", test_data_single_digits)
def test_is_armstrong_single_digits(test_input, expected):
    """Test of is_armstrong for single digit numbers"""
    assert is_armstrong(test_input) == expected


@pytest.mark.parametrize("test_input,expected", test_data_true)
def test_is_armstrong_true(test_input, expected):
    """Test of is_armstrong for really armstrong numbers"""
    assert is_armstrong(test_input) == expected


@pytest.mark.parametrize("test_input,expected", test_data_false)
def test_is_armstrong_false(test_input, expected):
    """Test of is_armstrong for not armstrong numbers"""
    assert is_armstrong(test_input) == expected


# tests for better_is_armstrong


@pytest.mark.parametrize("test_input,expected", test_data_single_digits)
def test_better_is_armstrong_single_digits(test_input, expected):
    """Test of better_is_armstrong for single digit numbers"""
    assert better_is_armstrong(test_input) == expected


@pytest.mark.parametrize("test_input,expected", test_data_true)
def test_better_is_armstrong_true(test_input, expected):
    """Test of better_is_armstrong for really armstrong numbers"""
    assert better_is_armstrong(test_input) == expected


@pytest.mark.parametrize("test_input,expected", test_data_false)
def test_better_is_armstrong_false(test_input, expected):
    """Test of better_is_armstrong for not armstrong numbers"""
    assert better_is_armstrong(test_input) == expected
