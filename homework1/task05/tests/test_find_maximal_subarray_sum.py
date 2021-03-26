from homework1.task05 import find_maximal_subarray_sum


def test_maximal_subarray_sum_happy_path():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    actual_result = find_maximal_subarray_sum(nums, k)
    assert actual_result == 16


def test_maximal_subarray_sum_k_is_equal_to_array_length():
    nums = [-6, 5, 0, -3, 13, 3, 0]
    k = 7
    actual_result = find_maximal_subarray_sum(nums, k)
    assert actual_result == 12


def test_maximal_subarray_sum_k_is_1():
    nums = [-6, 5, 0, -3, 13, 3, 0]
    k = 1
    actual_result = find_maximal_subarray_sum(nums, k)
    assert actual_result == 13


def test_maximal_subarray_sum_k_is_0():
    nums = [1, 2, 0, -3, 1, 3, 0]
    k = 0
    actual_result = find_maximal_subarray_sum(nums, k)
    assert actual_result == 0


def test_maximal_subarray_sum_k_is_greater_than_array_length():
    nums = [1, 2, 0, -3, 1, 3, 0]
    k = 8
    actual_result = find_maximal_subarray_sum(nums, k)
    assert actual_result is None
