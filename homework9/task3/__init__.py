import os


def get_paths(dir_path, extension):
    paths = []
    for file in [f for f in os.listdir(dir_path) if f.endswith("." + extension)]:
        paths.append(os.path.join(dir_path, file))
    return paths


def default_tokenizer(text):
    return text.splitlines()


def universal_file_counter(dir_path, file_extension, tokenizer=None):
    counts = 0
    if tokenizer is None:
        tokenizer = default_tokenizer
    paths = get_paths(dir_path, file_extension)
    for path in paths:
        with open(path) as f:
            for line in f:
                counts += len(tokenizer(line))

    return counts
