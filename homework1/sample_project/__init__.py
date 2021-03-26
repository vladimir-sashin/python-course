def check_power_of_2(a: int) -> bool:
    if a == 0:
        return False
    else:
        return not (bool(a & (a - 1)))
