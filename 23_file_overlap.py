def read_file(filename: str) -> int:
    with open(filename, 'r') as file:
        text = file.readlines()
    return len(text)


if __name__ == '__main__':
    res = read_file('files/23primenumbers.txt')
    print(res)
