def is_in_interval(filepath):
    try:
        with open(filepath) as f:
            if 1 <= float(f.readline()) < 3:
                return True
    except Exception as error:
        raise ValueError(
            "Invalid file or path, or file doesn't contain a number in the first line"
        ) from error
    return False
