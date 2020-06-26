from collections import Counter
from typing import List


def read_file(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        text = file.read().split('\n')
    return text


def read_from_file(data: List[str]) -> dict:
    counter = Counter(data)
    return counter


if __name__ == '__main__':
    txt = read_file('files/22names.txt')
    res = read_from_file(data=txt)
    print(res)
