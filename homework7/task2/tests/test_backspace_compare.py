from homework7.task2 import backspace_compare


def test_equal_words_without_backspaces():
    assert backspace_compare("abc", "abc")


def test_equal_words_with_backspace():
    assert backspace_compare("ab#c", "ao#c")


def test_equal_words_with_multiple_backspaces():
    assert backspace_compare("qw#ert#y", "qs#erf#y")


def test_equal_words_with_backspaces_and_different_length():
    assert backspace_compare("qw#e#rty", "qz#rty")


def test_equal_words_with_multiple_backspaces_in_a_row():
    assert backspace_compare("qwe###rty", "xyz###rty")


def test_equal_words_with_backspaces_in_the_beginning():
    assert backspace_compare("###abc", "##abc")


def test_equal_words_with_backspaces_in_the_end():
    assert backspace_compare("abc#", "abd#")


def test_not_equal_words_without_backspaces():
    assert backspace_compare("qwe", "awe") is False


def test_not_equal_words_with_backspace():
    assert backspace_compare("qb#c", "ao#c") is False


def test_not_equal_words_with_multiple_backspaces():
    assert backspace_compare("ab#cdef#g", "abc#de#fg") is False


def test_not_equal_words_with_backspaces_and_different_length():
    assert backspace_compare("qw#e#rty", "qqty") is False


def test_not_equal_words_with_multiple_backspaces_in_a_row():
    assert backspace_compare("qwe###rty", "xyzr###ty") is False


def test_not_equal_words_with_backspaces_in_the_beginning():
    assert backspace_compare("###abc", "##abd") is False


def test_not_equal_words_with_backspaces_in_the_end():
    assert backspace_compare("abc#", "acd#") is False
