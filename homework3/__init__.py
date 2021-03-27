def cache_decorator(func):
    cached = {}

    def cache(*args):
        if args in cached:
            return cached[args]
        else:
            func_output = func(*args)
            cached.update({args: func_output})
            return func_output

    return cache


@cache_decorator
def f():
    return input('? ')


f()
