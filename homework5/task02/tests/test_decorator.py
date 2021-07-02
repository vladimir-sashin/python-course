import functools

from homework5.task02 import print_result


# preparing test data - original function 'custom_sum' and decorating it by 'print_result'
@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


def test_save_info_copies_attributes():
    """Test for 'save_info', 'print_result' decorators:
    'save_info' decorator copies __doc__ and __name__ attributes of the original function that is decorated by
    'print_result'.
    Expected result: .__doc__ and .__name__ of the original function == .__doc__ and .__name__ of the function returned
    by 'save_info' decorator."""

    assert (custom_sum.__doc__, custom_sum.__name__) == (
        "This function can sum any objects which have __add___",
        "custom_sum",
    )


def test_decorated_function_returns_original_output(capsys):
    """Test for 'save_info', 'print_result' decorators:
    Directly call original function that is decorated by 'print_result'.
    Expected result - original (not changed) output of the function is:
        1. returned
        2. printed."""

    returned = custom_sum(1, 2, 3, 4)
    captured = capsys.readouterr()
    assert (returned, captured.out) == (10, "10\n")


def test_save_info_copies_original_function_to_attribute(capsys):
    """Test for 'save_info', 'print_result' decorators:
    'save_info' decorator copies original function that is decorated by 'print_result'.
    Expected result:
    Calling .__original_func of the function returned by 'save_info' decorator returns output of the original function
    without printing."""

    without_print = custom_sum.__original_func
    result = without_print(1, 2, 3, 4)
    captured = capsys.readouterr()
    assert (result, captured.out) == (10, "")
