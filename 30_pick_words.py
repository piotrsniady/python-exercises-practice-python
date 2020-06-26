import random


def pick_word(filename: str) -> str:
    with open(file=filename, mode="r") as file:
        text = file.readlines()

    chosen_word = random.choice(text)
    return chosen_word


word = pick_word(filename="stopwords_dictionary.txt")
print(word)
