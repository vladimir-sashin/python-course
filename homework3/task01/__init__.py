def limited_cache(times):
    def cache_decorator(func):
        cached = {}
        counter = 0

        def cache(*args):
            nonlocal counter
            if args in cached and counter < times:
                counter += 1
                return cached[args]
            else:
                func_output = func(*args)
                cached.update({args: func_output})
                counter = 0
                return func_output

        return cache

    return cache_decorator


@limited_cache(times=2)
def f():
    return input("? ")
