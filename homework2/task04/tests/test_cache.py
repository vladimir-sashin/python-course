from homework2.task04 import cache_decorator


@cache_decorator
def function_sample(a, b):
    print("inside the function")
    return (a ** b) ** 2


def test_cache_decorator():
    some = 100, 200

    val_1 = function_sample(*some)
    val_2 = function_sample(*some)

    assert val_1 is val_2
