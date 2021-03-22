"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


def custom_ranger(*args):
    def custom_range(func, start=None, stop=None, step=None):
        iterable = func
        if not stop:
            stop_index = len(iterable) - 1
        else:
            stop_index = iterable.find(stop)
        if not step:
            step = 1
        if not start:
            start_index = 0
        else:
            start_index = iterable.find(start)

        def custom_generator(start_index, stop_index, step):
            if step > 0:
                while start_index < stop_index:
                    yield iterable[start_index]
                    start_index += step
            else:
                while start_index > stop_index:
                    yield iterable[start_index]
                    start_index += step

        return list(custom_generator(start_index, stop_index, step))

    if len(args) == 2:
        func = args[0]
        start = None
        stop = args[1]
        return custom_range(func, start, stop)
    else:
        return custom_range(*args)
