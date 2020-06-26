import json
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt


def open_json_file(filename: str) -> any:
    with open(filename, 'r') as file:
        data = file.read()

    obj = json.loads(data)
    return obj


def count_months(file: dict) -> dict:
    month = [value[5:7] for key, value in file.items()]
    month_counter = Counter(month)
    return month_counter


def plot_histogram(src: dict) -> None:
    x_ax = np.arange(len(src))
    plt.bar(x_ax, src.values(), align='center', width=0.5)
    plt.xticks(x_ax, src.keys())
    plt.xlabel('Month')
    plt.ylabel('Occurrences')
    plt.show()


if __name__ == '__main__':
    json_file = open_json_file('files/birthdays.json')
    res = count_months(file=json_file)
    plot_histogram(src=res)
