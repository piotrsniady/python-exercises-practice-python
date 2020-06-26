from datetime import datetime


def input_validation(value: str, name_input: bool) -> (str, int):
    if name_input:
        val = ''.join(char for char in value if not char.isdigit())
        return val.capitalize()
    else:
        val = ''.join([char for char in value if char.isdigit()])
        return int(val)


def character_input() -> None:
    current_year = datetime.now().year

    name = input('Enter your name: ')
    correct_name = input_validation(name, name_input=True)

    input_age = input('Enter your age: ')
    age = input_validation(input_age, name_input=False)

    hundred_year = (current_year - age) + 100

    print(f'{correct_name}, you will be 100 years old in {hundred_year}')


if __name__ == '__main__':
    character_input()
