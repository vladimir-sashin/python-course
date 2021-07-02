def save_info(source):
    def decorate(destination):
        destination.__doc__ = source.__doc__
        destination.__name__ = source.__name__
        destination.__original_func = source
        return destination

    return decorate


def print_result(func):
    @save_info(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper
