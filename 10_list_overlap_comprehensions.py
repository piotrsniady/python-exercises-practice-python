def list_overlap_comprehensions(num_li_1: list, num_li_2: list) -> set:
    return set(num_li_1).intersection(set(num_li_2))


if __name__ == '__main__':
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    res = list_overlap_comprehensions(a, b)
    print(res)
