import numpy as np

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    lines = [x.strip() for x in lines]
    coords = [(int(x), int(y)) for x, y in [x.split(', ') for x in lines]]

    # Assign names to coordinates
    # coords = {i: coords[i] for i in range(len(coords))}

    # Put coordinates on matrix
    arr = np.zeros((400, 400, 2), dtype=np.uint16)
    for i, coord in enumerate(coords):
        # Z=0 is the distance
        arr[coord[0], coord[1], 0] = 0

        # Z=1 is the coordinate "name"
        arr[coord[0], coord[1], 1] = i

    max(coords)
    400 ** 2
    arr
    coords

    np.zeros((2, 2), dtype=np.int8)

    coords

if __name__ == '__main__':
    main()

