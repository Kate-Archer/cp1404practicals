password = input("What is the password?: ")
MINIMUM_LENGTH = 4
while len(password) < MINIMUM_LENGTH:
    print("Password too short. (Min length of 4)")
    password = input("What is the password?: ")
print(len(password) * "*")
