import string

from homework2.task05 import custom_ranger


def test_custom_ranger_2_args():
    assert custom_ranger(string.ascii_lowercase, "g") == ["a", "b", "c", "d", "e", "f"]


def test_custom_ranger_3_args():
    assert custom_ranger(string.ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]


def test_custom_ranger_4_args_positive_step():
    assert custom_ranger(string.ascii_lowercase, "g", "p", 2) == [
        "g",
        "i",
        "k",
        "m",
        "o",
    ]


def test_custom_ranger_4_args_negative_step():
    assert custom_ranger(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]
