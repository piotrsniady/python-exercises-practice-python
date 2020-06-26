def string_lists(string: str) -> str:
    return str([f'Given word: {string} is a palindrome' if string == string[::-1] else f'Given word: {string} is not a palindrome'])


if __name__ == '__main__':
    given_string = input('Enter word: ')
    res = string_lists(given_string)
    print(res)
