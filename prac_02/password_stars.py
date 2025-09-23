def main():
    """ Give a valid password """
    password = get_password()
    print_password(password)


def print_password(password: str):
    print(len(password) * "*")


def get_password() -> str:
    password = input("What is the password?: ")
    minimum_length = 4
    while len(password) < minimum_length:
        print("Password too short. (Min length of 4)")
        password = input("What is the password?: ")
    return password


main()
