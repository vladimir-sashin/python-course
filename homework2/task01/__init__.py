"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""

import re
import unicodedata


def get_longest_diverse_words(file_path: str) -> list:
    with open(file_path, encoding="unicode_escape") as f:
        text = f.read().lower()
        text_without_hyphenation = re.sub(r"-\s", r"", text)
        words = re.split(r"\W+", text_without_hyphenation)
        words_with_length = {word: len(set(word)) for word in words if word != ""}
        return sorted(words_with_length, key=words_with_length.get, reverse=True)[:10]


def get_rarest_char(file_path: str) -> str:
    with open(file_path, encoding="unicode_escape") as f:
        text = f.read()
        text_without_whitespaces = re.sub(r"\s", r"", text)
        chars_quantity = {
            char: text_without_whitespaces.count(char)
            for char in set(text_without_whitespaces)
        }
        return min(chars_quantity, key=chars_quantity.get)


def get_list_of_rarest_chars(file_path: str) -> list:
    """I'd like to suggest the following solution for the 2nd subtask, because in case if we have more than 1 rarest
    char, this is more correct. The function returns a list of rarest characters that have the same frequency"""
    with open(file_path, encoding="unicode_escape") as f:
        text = f.read()
        text_without_whitespaces = re.sub(r"\s", r"", text)
        chars_quantity = {
            char: text_without_whitespaces.count(char)
            for char in set(text_without_whitespaces)
        }
        how_many_rarest_chars = 0
        for k in chars_quantity:
            if (
                chars_quantity[k]
                == chars_quantity[min(chars_quantity, key=chars_quantity.get)]
            ):
                how_many_rarest_chars += 1
        return sorted(chars_quantity, key=chars_quantity.get)[:how_many_rarest_chars]


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode_escape") as f:
        text = f.read()
        only_punctuation_chars = [
            char
            for char in text
            if re.fullmatch(r"P[a-z]*", unicodedata.category(char))
        ]
        return len(only_punctuation_chars)


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode_escape") as f:
        text = f.read()
        non_ascii_chars_quantity = 0
        for char in text:
            if ord(char) > 127:
                non_ascii_chars_quantity += 1
        return non_ascii_chars_quantity


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, encoding="unicode_escape") as f:
        text = f.read()
        non_ascii_chars = [char for char in text if ord(char) > 127]
        non_ascii_chars_frequencies = {
            char: non_ascii_chars.count(char) for char in non_ascii_chars
        }
        if non_ascii_chars_frequencies != {}:
            return max(non_ascii_chars_frequencies, key=non_ascii_chars_frequencies.get)
        else:
            return ""
