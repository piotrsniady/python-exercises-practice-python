from random import randint


def game():
    random_number = randint(1, 10)
    guess = int(input("Please enter your guess: "))
    if guess not in range(1, 11):
        print("[WARNING] You entered invalid number. Only numbers from 1 to 10 are available.")
        exit(1)
    else:
        while random_number != "guess":
            if guess < random_number:
                print("Your guess is too low")
                guess = int(input("Please enter your guess: "))
            elif guess > random_number:
                print("Your guess is too high")
                guess = int(input("Please enter your guess: "))
            else:
                print("GUESSED")
                break


if __name__ == '__main__':
    game()
