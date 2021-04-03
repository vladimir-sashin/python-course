from functools import reduce


def is_armstrong(number: int) -> bool:
    digits = [int(number) for number in str(number)]
    raised_digits = [digit ** len(digits) for digit in digits]
    raised_digits_sum = reduce((lambda x, y: x + y), raised_digits)
    return raised_digits_sum == number


# print(is_armstrong(10))


def better_is_armstrong(number: int) -> bool:
    digits = [int(number) for number in str(number)]

    def raise_to_the_power(x, power=len(digits)):
        return x ** power

    raised_digits_sum = reduce((lambda x, y: x + y), map(raise_to_the_power, digits))
    return raised_digits_sum == number


# print(better_is_armstrong(0))
