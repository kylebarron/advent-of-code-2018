
def main():
    with open('input.txt') as f:
        lines = f.readlines()

    line = [x.strip() for x in lines][0]
    numbers = [int(x) for x in line.split(' ')]
    metadata = []

    def parse_input(numbers):
        num_children = numbers.pop(0)
        num_metadata = numbers.pop(0)

        for child in range(num_children):
            parse_input(numbers)

        for i in range(num_metadata):
            metadata.append(numbers.pop(0))

    parse_input(numbers)
    print('Part 1:')
    print(sum(metadata))


if __name__ == '__main__':
    main()
