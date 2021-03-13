"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def fibonacci_generator(quantity: int) -> list:
    a, b = (0, 1)
    for i in range(quantity):
        yield a
        (a, b) = (b, a + b)


def check_fibonacci(data: Sequence[int]) -> bool:
    seq_length = len(data)
    if seq_length < 3:
        return False
    elif data == list(fibonacci_generator(seq_length)):
        return True
    else:
        return False


seq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
print(check_fibonacci(seq))
print(len(seq))