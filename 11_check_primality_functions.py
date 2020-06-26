def check_primality_functions(n: int) -> None:
    divisors = [j for j in [i for i in range(1, n+1)] if n % j == 0]
    if len(divisors) == 2:
        print(f'Given number is prime. The divisors are:{divisors}')
        exit(1)
    else:
        print(f'Given number is not prime. The divisors are:{divisors}')
        exit(1)


def clean_value(value: str) -> int:
    val = ''.join(i for i in value if i.isdigit())
    print('Processed values is:', val)
    return int(val)


if __name__ == '__main__':
    number = input('Enter the number: ')
    cleaned_value = clean_value(number)
    check_primality_functions(cleaned_value)
