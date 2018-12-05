def main():
    with open('input1.txt') as f:
        lines = f.readlines()

    lines = [x.strip() for x in lines]
    print(eval(''.join(lines)))

if __name__ == '__main__':
    main()
