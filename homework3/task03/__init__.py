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
    return Filter(filter_funcs)
