def main():
    with open('input.txt') as f:
        lines = f.readlines()

    string = lines[0].strip()

    last_length = 0
    i = 0
    while len(string) != last_length:
        print('iteration: ', i)
        print('string length: ', len(string))
        i += 1
        last_length = len(string)
        string = reduce_string(string)

    print('Part 1: ', len(string))


def reduce_string(string: str) -> str:
    """Make a single pass to remove reactions from string
    """

    reaction_indices = []
    for obj1, obj2 in zip(enumerate(string), enumerate(string[1:])):
        index1, letter1 = obj1
        index2, letter2 = obj2
        index2 += 1

        if not is_reaction(letter1, letter2):
            continue

        if index1 in reaction_indices:
            continue

        reaction_indices.extend([index1, index2])

    return [x for ind, x in enumerate(string) if ind not in reaction_indices]


def is_reaction(letter1: str, letter2):
    if letter1 == letter2:
        return False

    if letter1.lower() == letter2.lower():
        return True

    return False


if __name__ == '__main__':
    main()
