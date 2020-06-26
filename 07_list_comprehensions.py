def list_comprehensions(num_list: list) -> list:
    return [j for j in num_list if j % 2 == 0]


if __name__ == '__main__':
    numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    res = list_comprehensions(num_list=numbers)
    print(res)
