def fibonacci_sequence(quantity) -> list:
    a, b = (0, 1)
    for i in range(quantity):
        yield a
        (a, b) = (b, a + b)


fibonacci = list(fibonacci_sequence(10))
print(fibonacci)