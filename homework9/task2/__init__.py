from contextlib import contextmanager


class Suppressor:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return isinstance(exc_val, self.exception)


@contextmanager
def suppressor(exception):
    try:
        yield
    except exception:
        pass
