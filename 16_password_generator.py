import random
import string


def generate_string(n: int, opt: str, li=None) -> str:
    opt_list = ["char", "num"]
    if not isinstance(opt, str):
        print("Given opt argument is not a string format.")
        quit()
    elif opt not in opt_list:
        print(f"Given option does not exist. Available options are: {opt_list}.")
        quit()
    else:
        if opt == "num":
            return ''.join([str(i) for i in random.sample(range(0, 9), n)])
        if opt == "char" and li:
            return ''.join([random.choice(li) for _ in range(1, n + 1)])
        else:
            print("You dod not give the list with data.")


def password_generator(n: str, add_spec_chars: bool, add_nums: bool) -> str:
    list_of_letters = string.ascii_letters
    list_of_spec_chars = ['@', '#', '!', '$', '&', '*', '?', '%']

    n = int(n)
    special_characters = ""
    numbers = ""

    if add_spec_chars and not add_nums:
        letters = generate_string(li=list_of_letters, n=n, opt='char')
        special_characters = generate_string(li=list_of_spec_chars, n=n, opt='char')
    elif add_nums and not add_spec_chars:
        letters = generate_string(li=list_of_letters, n=n, opt='char')
        numbers = generate_string(n=n, opt='num')
    elif add_spec_chars and add_nums:
        letters = generate_string(li=list_of_letters, n=n, opt='char')
        special_characters = generate_string(li=list_of_spec_chars, n=n, opt='char')
        numbers = generate_string(n=n, opt='num')
    else:
        letters = generate_string(li=list_of_letters, n=n, opt='char')

    password = letters + special_characters + numbers
    shuffled_password = ''.join(random.sample(password, n))
    return shuffled_password


if __name__ == '__main__':
    while True:
        length = input('Please enter the length of the password: ')
        if int(length) in range(12, 17):
            generated_password = password_generator(n=length, add_spec_chars=False, add_nums=False)
            print(generated_password)
            quit()
