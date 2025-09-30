"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = False  # Set to fault, it is not required
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # Not return a password if the password is below the minimum length or
    # above the maximum length as it is invalid
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    # Set the characters to 0 initially
    number_of_digit = 0
    number_of_lower = 0
    number_of_upper = 0
    number_of_special = 0
    for character in password:
        # Count the number of different character types in password
        if character.isdigit():
            number_of_digit += 1
        elif character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1

    # Return False if any of the 'normal' counts are zero
    if number_of_digit == 0 or number_of_lower == 0 or number_of_upper == 0:
        return False
    # Count the amount of special characters if the special characters required is set to True
    # and return False if it's zero
    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == 0:
        return False

    # Return True if all other checks have not returned False (password must be valid)
    return True


main()
