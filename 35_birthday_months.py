import json
from collections import Counter
from typing import List


def open_json_file() -> dict:
    with open('files/birthdays.json', 'r') as file:
        data = file.read()

    obj = json.loads(data)
    return obj


def count_months(file: dict) -> List[dict]:
    month = [value[5:7] for key, value in file.items()]
    return list(Counter(month))


if __name__ == '__main__':
    json_file = open_json_file()
    res = count_months(file=json_file)
    print(res)
