birthday_dict = {
    'Albert Einstein': '1879-03-14',
    'Nikola Tesla': '1856-07-10',
    'Isaac Newton': '1643-01-04',
    'Michael Faraday': '1791-09-22'
}


def print_menu():
    print('Welcome to the birthday dictionary. We know the birthdays of: \n')
    for key in birthday_dict.keys():
        print(key)


def select_name():
    print("\nWho's birthday do you want to look up? \n")
    name = input('Enter the name: ')
    for key, value in birthday_dict.items():
        if name not in birthday_dict.keys():
            print(f'There is no such name as {name} in the dictionary.')
            exit(1)
        else:
            if name == key:
                print(key, value)


if __name__ == '__main__':
    print_menu()
    select_name()
