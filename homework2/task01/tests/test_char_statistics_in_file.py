from homework2.task01 import (
    get_longest_diverse_words,
    get_rarest_char,
    get_list_of_rarest_chars,
    count_punctuation_chars,
    count_non_ascii_chars,
    get_most_common_non_ascii_char,
)
import os


def get_file_path(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)


expected_longest_words = [
    "bedenklichen",
    "verbirgt",
    "vielmehr",
    "waldgang",
    "hinter",
    "ausflug",
    "gefaßt",
    "machen",
    "idylle",
    "keine",
]


def test_get_longest_diverse_words():
    assert (
        get_longest_diverse_words(get_file_path("data.txt")) == expected_longest_words
    )


def test_get_longest_diverse_words_may_repeat():
    assert (
        get_longest_diverse_words(get_file_path("data_words_repeat.txt"))
        == expected_longest_words
    )


def test_get_longest_diverse_words_no_words():
    assert get_longest_diverse_words(get_file_path("data_no_words.txt")) == []


def test_get_rarest_char():
    assert get_rarest_char(get_file_path("data_rarest_char.txt")) == "\u00df"


def test_get_list_of_rarest_chars():
    assert sorted(
        get_list_of_rarest_chars(get_file_path("data_rarest_characters.txt"))
    ) == sorted(["D", "r", "W", "\u2014", "t", "k", "I", "y", "."])


def test_count_punctuation_chars():
    assert count_punctuation_chars(get_file_path("data.txt")) == 5


def test_count_punctuation_chars_equals_0():
    assert count_punctuation_chars(get_file_path("data_without_punctuation.txt")) == 0


def test_count_non_ascii_chars():
    assert count_non_ascii_chars(get_file_path("data.txt")) == 3


def test_count_non_ascii_chars_equals_0():
    assert count_non_ascii_chars(get_file_path("data_no_non_ascii.txt")) == 0


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char(get_file_path("data.txt")) == "\u00df"


def test_get_most_common_non_ascii_char_doesnt_exist():
    assert get_most_common_non_ascii_char(get_file_path("data_no_non_ascii.txt")) == ""
