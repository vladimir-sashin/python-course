def extract_values_from_tree(d, element):
    stack = list(d.values())
    counter = 0

    while stack:
        print(stack)
        value = stack.pop()
        if value == element:
            counter += 1
        elif isinstance(value, dict):
            stack.extend(value.values())
        elif isinstance(value, (list, set, tuple)):
            stack.extend(value)
    return counter
