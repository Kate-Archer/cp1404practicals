def main():
    """ give a valid password """
    password = input("What is the password?: ")
    minimum_length = 4
    while len(password) < minimum_length:
        print("Password too short. (Min length of 4)")
        password = input("What is the password?: ")
    print(len(password) * "*")


main()
