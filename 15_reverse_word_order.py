def reverse_word_order(string: str) -> str:
    if not isinstance(string, str):
        print("[WARNING] Given value is not string type.")
        quit()
    elif len(string) == 0:
        print("Given sentence was empty.")
        quit()
    return string[::-1]


if __name__ == '__main__':
    sentence = input('Please enter a sentence: ')
    res = reverse_word_order(sentence)
    print(res)
