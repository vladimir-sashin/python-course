from functools import partial


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(i(item) for i in self.functions)]


# example of usage:
# positive_even = Filter(lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int))
# positive_even.apply(range(100)) should return only even numbers from 0 to 99

# positive_even = Filter([lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)])
# print(positive_even.apply(range(100)))


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, filter_value in keywords.items():

        def keyword_filter_func(value, key=key, filter_value=filter_value):
            try:
                return value[key] == filter_value
            except KeyError:
                return False

        filter_funcs.append(keyword_filter_func)
    # print(filter_funcs)
    return Filter(filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]
# my_filter = make_filter(name='polly', type='bird')
# print(my_filter.apply(sample_data))

# data = [dict(a=1, b=1), dict(a=1, b=2)]
# print(make_filter(b=1, a=1).apply(sample_data))

# print(make_filter(name='polly', type='bird').apply(sample_data))  # should return only second entry from the list


def custom_ranger(*args):
    def custom_range(func, start=None, stop=None, step=None):
        iterable = func
        if not stop:
            stop_index = len(iterable) - 1
        else:
            stop_index = iterable.index(stop)
        if not step:
            step = 1
        if not start:
            start_index = 0
        else:
            start_index = iterable.index(start)

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


# print(custom_ranger(list(range(10)), 0, 5, 2))


"""def float_range(start, stop, step):
    while start < stop:
        yield start
        start += step


print(list(float_range(0, 100, 0.5)))"""
