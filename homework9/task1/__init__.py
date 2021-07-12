from heapq import merge


def merge_sorted_files_heapq(file_list):
    """Merges sorted sequences of integers written line by line in the files from 'file_list' argument,
    returns generator. Based on 'merge()' from 'heapq'"""
    gens = []
    for file in file_list:
        file_gen = read_file(file)
        l = (int(num) for num in file_gen)
        gens.append(l)
    return merge(*gens)


def merge_sorted_files(file_list):
    """Another variant of a function that merges sorted lists from multiple files that doesn't use heapq.merge"""
    generators = []
    for file in file_list:
        file_gen = read_file(file)
        lines = (int(num) for num in file_gen)
        generators.append(lines)
    yield from merge_generators(generators)


def merge_generators(generators):
    generator_tops = {generator: next(generator) for generator in generators}
    while generator_tops:
        active_generator, min_value = min(generator_tops.items(), key=lambda x: x[1])
        yield min_value
        try:
            generator_tops[active_generator] = next(active_generator)
        except StopIteration:
            del generator_tops[active_generator]


def read_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.rstrip()
