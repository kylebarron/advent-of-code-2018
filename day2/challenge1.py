def main():
    with open('input.txt') as f:
        lines = f.readlines()

    lines = [x.strip() for x in lines]
    truths = []
    for word in lines:
        truths.append(search_word(word))

    print(sum([x[0] for x in truths]) * sum([x[1] for x in truths]))

def search_word(word: str) -> (bool, bool):
    """Search each word in list

    Returns:
        (has exactly 2 of any letter, has exactly 3 of any letter)
    """

    char_dict = {}
    for letter in word:
        char_dict[letter] = char_dict.get(letter, 0) + 1

    return (2 in char_dict.values(), 3 in char_dict.values())


if __name__ == '__main__':
    main()
