import string


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    line = lines[0].strip()

    part_1_string = react_polymer(line)
    print('Part 1: ', len(part_1_string))

    data = {}
    for lower, upper in zip(string.ascii_lowercase, string.ascii_uppercase):
        line_edited = [x for x in line if x not in [lower, upper]]
        data[lower] = len(react_polymer(line_edited))

    print('Part 2: ', min(data.values()))


def react_polymer(line: str) -> str:
    """Perform all reactions of string"""

    last_length = 0
    i = 0
    while len(line) != last_length:
        print('iteration: ', i)
        print('string length: ', len(line))
        i += 1
        last_length = len(line)
        line = reduce_string(line)

    return line


def reduce_string(line: str) -> str:
    """Make a single pass to remove reactions from string"""

    reaction_indices = []
    for obj1, obj2 in zip(enumerate(line), enumerate(line[1:])):
        index1, letter1 = obj1
        index2, letter2 = obj2
        index2 += 1

        if not is_reaction(letter1, letter2):
            continue

        if index1 in reaction_indices:
            continue

        reaction_indices.extend([index1, index2])

    return [x for ind, x in enumerate(line) if ind not in reaction_indices]


def is_reaction(letter1: str, letter2):
    if letter1 == letter2:
        return False

    if letter1.lower() == letter2.lower():
        return True

    return False


if __name__ == '__main__':
    main()
