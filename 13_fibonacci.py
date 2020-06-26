def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def input_validation(value: str) -> int:
    val = ''.join(i for i in value if i.isdigit())
    return int(val)


if __name__ == '__main__':
    number = input('Enter the number: ')
    val_input = input_validation(number)
    for j in range(val_input):
        print(fib(j))
