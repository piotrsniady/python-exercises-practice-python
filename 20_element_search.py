from typing import List


def check_number(value: str) -> int:
    if not value.isdigit():
        print('[WARNING] Given value is not a number!')
        quit()
    return int(value)


def element_search(nums: list, n: int) -> List[bool]:
    sorted_nums = set(nums)
    is_number = [True if n in sorted_nums else False]
    print('Is the number in the given list?')
    return is_number


if __name__ == '__main__':
    li = [4, 8, 1, 4, 9, 12, 6, 7]
    number = input('Enter the number: ')
    val = check_number(value=number)
    result = element_search(nums=li, n=val)
    print(result)
