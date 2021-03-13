from check_fibonacci.task02 import check_fibonacci, fibonacci_generator


def test_check_fibonacci_generator_length_3():
    length = 3
    actual_result = list(fibonacci_generator(length))
    assert actual_result == [0, 1, 1]


def test_check_fibonacci_generator_length_21():
    length = 21
    actual_result = list(fibonacci_generator(length))
    assert actual_result == [
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        144,
        233,
        377,
        610,
        987,
        1597,
        2584,
        4181,
        6765,
    ]


def test_check_fibonacci_length_3():
    sequence = [0, 1, 1]
    actual_result = check_fibonacci(sequence)
    assert actual_result is True


def test_check_fibonacci_happy():
    sequence = [
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        144,
        233,
        377,
        610,
        987,
        1597,
        2584,
        4181,
        6765,
    ]
    actual_result = check_fibonacci(sequence)
    assert actual_result is True


def test_check_fibonacci_length_2():
    sequence = [0, 1]
    actual_result = check_fibonacci(sequence)
    assert actual_result is False


def test_check_fibonacci_empty():
    sequence = []
    actual_result = check_fibonacci(sequence)
    assert actual_result is False


def test_check_fibonacci_length_1():
    sequence = [0]
    actual_result = check_fibonacci(sequence)
    assert actual_result is False


def test_check_fibonacci_partial_success():
    sequence = [0, 1, 1, 3, 5, 9, 13]
    actual_result = check_fibonacci(sequence)
    assert actual_result is False


def test_check_fibonacci_last_num_invalid():
    sequence = [0, 1, 1, 3, 5, 8, 15]
    actual_result = check_fibonacci(sequence)
    assert actual_result is False
