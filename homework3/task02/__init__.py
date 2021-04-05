import hashlib
import random
import struct
import time
from multiprocessing import Pool
from timeit import default_timer


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def speed_up_slow_calculate():
    start = default_timer()
    numbers = (num for num in range(501))
    with Pool(32) as pool:
        pool.map(slow_calculate, numbers)
    end = default_timer()
    print(f"Elapsed time: {end - start}")
    return end - start
