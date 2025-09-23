"""
CP1404 - Practical
Get a password with minimum length and display asterisks
"""
# Define the minimum password length (constant)
MINIMUM_LENGTH = 4


def main():
    """Get and print a valid password with functions."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)



# Attempt 2:
def get_password(MINIMUM_LENGTH):
    """Get password, ensuring it meets the minimum_length requirement."""
    password = input(f"Enter password (minimum length {MINIMUM_LENGTH} characters): ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password too short. (Minimum length of {MINIMUM_LENGTH})")
        password = input(f"Enter password (minimum length {MINIMUM_LENGTH} characters): ")
    return password


def print_asterisks(sequence):
    """Print as many asterisks as there are characters in the passed-in sequence."""
    print('*' * len(sequence))


main()

# Attempt 1:
# def get_password() -> str:
#     """Get password, ensuring it meets the minimum length requirement."""
#     password = input("What is the password?: ")
#     while len(password) < MINIMUM_LENGTH:
#         print("Password too short. (Min length of 4)")
#         password = input("What is the password?: ")
#     return password
#
# def print_asterisks(password: str):
#     """Print the same amount of asterisks as characters in the password."""
#     print(len(password) * "*")
