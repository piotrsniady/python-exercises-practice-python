from typing import List


def divisors(n: int) -> List[int]:
    return [j for j in [i for i in range(1, n+1)] if n % j == 0]


def validate_input(value: str) -> int:
    val = ''.join(i for i in value if i.isdigit())
    print('Processed values is:', val)
    return int(val)


if __name__ == '__main__':
    given_number = input('Enter the number: ')
    checked_val = validate_input(value=given_number)
    res = divisors(n=checked_val)
    print(res)
