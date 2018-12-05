def main():
    with open('input1.txt') as f:
        lines = f.readlines()

    lines = [x.strip() for x in lines]
    frequencies = {0}
    counter = 0
    i = -1
    while True:
        i += 1
        counter += eval(lines[i % len(lines)])
        if counter in frequencies:
            print(counter)
            break
        frequencies.add(counter)

if __name__ == '__main__':
    main()
