from homework1.task04 import check_sum_of_four


def test_check_sum_of_four_happy():
    a = [1, -6]
    b = [6, -4]
    c = [8, -7]
    d = [2, 0]
    actual_result = check_sum_of_four(a, b, c, d)
    assert actual_result == 2


def test_check_sum_of_four_empty_lists():
    a = []
    b = []
    c = []
    d = []
    actual_result = check_sum_of_four(a, b, c, d)
    assert actual_result == 0
