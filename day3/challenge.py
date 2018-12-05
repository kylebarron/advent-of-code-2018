import re
import numpy as np


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    lines = [x.strip() for x in lines]
    arr = np.zeros((1000, 1000), 'uint16')
    for code in lines:
        d = split_into_parts(code)
        arr[d['y_start']:d['y_end'], d['x_start']:d['x_end']] += 1

    print('Part 1:')
    print(np.sum(np.where(arr > 1, True, False)))

    for code in lines:
        d = split_into_parts(code)
        if check_area(arr, d):
            print('Part 2:')
            print(d['id'])
            break


def split_into_parts(code):
    regex = r'^#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)$'
    match = re.search(regex, code)

    x_start = int(match.group(2))
    x_end = x_start + int(match.group(4))
    y_start = int(match.group(3))
    y_end = y_start + int(match.group(5))

    return {
        'id': int(match.group(1)),
        'x_start': x_start,
        'x_end': x_end,
        'y_start': y_start,
        'y_end': y_end}

def check_area(arr, d):
    if np.all(arr[d['y_start']:d['y_end'], d['x_start']:d['x_end']] == 1):
        return True

    return False


if __name__ == '__main__':
    main()
