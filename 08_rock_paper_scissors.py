from random import choice

options = ['rock', 'paper', 'scissors']


def check_input(val: str) -> str:
    if val.lower() not in options:
        print('Given option is not in an options list.')
        quit()
    else:
        print('Your option: ', val.lower())
        return val.lower()


def generate_value() -> str:
    option = choice(options)
    print('Opponent option:', option)
    return option


def rock_paper_scissors(player1_option: str, player2_option: str) -> str:
    if player1_option == player2_option:
        return 'Draw'
    elif player1_option == 'rock' and player2_option == 'scissors':
        return 'You win'
    elif player1_option == 'scissors' and player2_option == 'rock':
        return 'Opponent wins'
    elif player1_option == 'scissors' and player2_option == 'paper':
        return 'You win'
    elif player1_option == 'paper' and player2_option == 'scissors':
        return 'Opponent wins'
    elif player1_option == 'paper' and player2_option == 'rock':
        return 'You win'
    else:
        return 'Opponent wins'


def game():
    end = 3
    while end != 0:
        print('Available options: \n + rock \n + paper \n + scissors.')
        given_option = input("Enter an option: ")
        check_value = check_input(val=given_option)
        rand_value = generate_value()
        game = rock_paper_scissors(player1_option=check_value, player2_option=rand_value)
        print(game)
        end -= 1


if __name__ == '__main__':
    game()
