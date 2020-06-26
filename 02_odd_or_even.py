def odd_or_even(n: int) -> str:
    if n % 2 == 0:
        return 'Given number is odd.'
    else:
        return 'Given number is even.'


def clean_number(value: str) -> int:
    val = ''.join(i for i in value if i.isdigit())
    print('The value is processed:', val)
    return int(val)


if __name__ == '__main__':
    given_number = input('Enter the number: ')
    num = clean_number(value=given_number)
    res = odd_or_even(n=num)
    print(res)
