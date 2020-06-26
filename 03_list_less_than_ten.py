numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def clean_value(value):
    val = ''.join(i for i in value if i.isdigit())
    print('Processed values is:', val)
    return int(val)


def validate_number(value: int) -> int:
    if value in range(min(numbers), max(numbers)):
        return value
    print(f'Given number is out of range. Acceptable range is: {min(numbers)}-{max(numbers)}')
    exit(1)


def less_than_ten(n: int) -> list:
    x = [i for i in numbers if i < n]
    return x


if __name__ == '__main__':
    given_num = input('Enter a number: ')
    clean_val = clean_value(given_num)
    val_num = validate_number(clean_val)
    res = less_than_ten(val_num)
    print(res)
