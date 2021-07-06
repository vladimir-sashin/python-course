def make_a_word(initial_word):
    word = []
    for char in initial_word:
        if char == "#":
            try:
                word.pop()
            except IndexError:
                pass
        else:
            word.append(char)
    return word


def backspace_compare(first, second):
    first, second = make_a_word(first), make_a_word(second)
    return first == second
