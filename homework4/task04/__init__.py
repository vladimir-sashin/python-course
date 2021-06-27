def fizzbuzz(n):
    """
    The function takes a number n as an input and returns a list of FizzBuzz numbers in range of [1,n].
    FizzBuzz numbers: https://en.wikipedia.org/wiki/Fizz_buzz

        Parameters:
            n (int): a positive integer

        Returns:
            fizzbuzz_list (list): a list of FizzBuzz numbers in range of [1,n]

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']

    >>> fizzbuzz(0)
    []
    """

    fizzbuzz_list = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz_list.append("fizz buzz")
        elif i % 3 == 0:
            fizzbuzz_list.append("fizz")
        elif i % 5 == 0:
            fizzbuzz_list.append("buzz")
        else:
            fizzbuzz_list.append(str(i))
    return fizzbuzz_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
