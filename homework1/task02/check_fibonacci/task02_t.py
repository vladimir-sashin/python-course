def _check_window(x: int, y: int, z: int) -> bool:
    return (x + y) == z


data_to_process = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]


assert len(data_to_process) >= 3

a, b, c = data_to_process[0], data_to_process[1], data_to_process[2]

while data_to_process:
    if not _check_window(a, b, c):
        raise ValueError("Invalid data")

    a, b, c = b, c, data_to_process[0]
    data_to_process = data_to_process[1:]

print("it's a fib sequence!")