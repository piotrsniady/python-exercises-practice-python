def list_overlap(li1: list, li2: list) -> set:
    print(f'The same numbers from \n{li1} \nand \n{li2} \nare:')
    return set(li1).intersection(set(li2))


if __name__ == '__main__':
    list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    res = list_overlap(li1=list1, li2=list2)
    print(res)
