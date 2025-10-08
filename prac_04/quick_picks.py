"""
CP1404/CP5632 Practical - Suggested Solution
Quick pick program
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Quick picks program - choose sets of random numbers based on user input."""
    number_of_quick_picks = int(input("How many quick picks do you wish to generate?: "))
    while number_of_quick_picks < 0:
        print("There must be at least 1 quick pick!")
        number_of_quick_picks = int(input("How many quick picks do you wish to generate?: "))

    for i in range(number_of_quick_picks):
        quick_pick = []  # Creates an empty list to store quick pick values of size i
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)  # Inner loop, runs 6 times
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)  # Ensures no duplicates
            quick_pick.append(number)  # Adds the unique number
        quick_pick.sort()  # Sorts list in ascending order
        print(" ".join(f"{number:2}" for number in quick_pick))  # Alligns nicely


main()
