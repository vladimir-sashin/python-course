from calculator.calc import check_power_of_2


def test_is_0_power_of_2():
    value = 0
    actual_result = check_power_of_2(value)
    assert actual_result is False


def test_is_1_power_of_2():
    value = 1
    actual_result = check_power_of_2(value)
    assert actual_result is True


def test_is_2_power_of_2():
    value = 2
    actual_result = check_power_of_2(value)
    assert actual_result is True


def test_is_5_power_of_2():
    value = 5
    actual_result = check_power_of_2(value)
    assert actual_result is False


def test_is_65536_power_of_2():
    value = 65536
    actual_result = check_power_of_2(value)
    assert actual_result is True
