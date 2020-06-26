import json


def open_json_file() -> dict:
    with open('files/birthdays.json', 'r') as file:
        data = file.read()

    obj = json.loads(data)
    return obj


def print_menu(data_dict: dict) -> None:
    print('Welcome to the_ birthday dictionary. We know the birthdays of:\n')
    for key in data_dict.keys():
        print(key)


def select_name(data_dict) -> None:
    print("\nWho's birthday do you want to look up? \n")
    name = input('Enter the name: ')
    for key, value in data_dict.items():
        if name not in data_dict.keys():
            print(f'There is no name {name} in dictionary.')
            exit(1)
        else:
            if name == key:
                print(key, value)


if __name__ == '__main__':
    dictionary = open_json_file()
    print_menu(data_dict=dictionary)
    select_name(data_dict=dictionary)
