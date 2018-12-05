import numpy as np


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    lines = [x.strip() for x in lines]
    n_words = len(lines)
    valid_boxes_arr = np.full((n_words, n_words), True)
    valid_boxes_arr = np.tril(valid_boxes_arr, -1)
    for (x, y), value in np.ndenumerate(valid_boxes_arr):
        if not value:
            continue

        word1 = lines[x]
        word2 = lines[y]
        if get_word_distance(word1, word2):
            print(get_common_letters(word1, word2))
            break


def get_word_distance(word1: str, word2: str) -> bool:
    """Get distance between two words

    Returns:
        True if exactly one letter apart in the same place. False otherwise
    """

    letters_different = 0
    for x, y in zip(word1, word2):
        if x != y:
            letters_different += 1
            if letters_different > 1:
                return False

    return True


def get_common_letters(word1: str, word2: str) -> str:
    """Get common letters of two words
    """

    common = ''
    for x, y in zip(word1, word2):
        if x == y:
            common += x

    return common


if __name__ == '__main__':
    main()
