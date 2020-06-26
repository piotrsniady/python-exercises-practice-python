from random import randint

cows = []
bulls = []


def cows_amount(n: int, guess: int) -> int:
    for i in str(n):
        for j in str(guess):
            if i == j:
                cows.append(i)
    return len(cows)


def check_if_in(n: int, guess: int) -> bool:
    for i in str(n):
        if i in str(guess):
            return True


def bulls_amount(n: int, guess: int) -> int:
    for i in str(n):
        for j in str(guess):
            if i == j and not check_if_in(n, guess):
                bulls.append(i)
    return len(bulls)


def clean_value(value: str) -> int:
    if len(value) != 4:
        print('[WARNING] Given number is incorrect. ONLY 4 digit number allowed.')
        quit()
    val = ''.join(i for i in value if i.isdigit())
    print('Processed values is:', val)
    return int(val)


if __name__ == '__main__':
    number = randint(1000, 9999)

    input_value = input('Enter a four digit number: ')
    guess_number = clean_value(value=input_value)

    cow = cows_amount(n=number, guess=guess_number)
    bull = bulls_amount(n=number, guess=guess_number)

    print(f"{cow} cows, {bull} bulls.")

