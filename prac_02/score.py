"""
CP1404/CP5632 - Practical 1
Program to determine score status
Fixed to determine score status, with function
"""

# Note 50 is included in the pass boundary

import random


def main():
    """Get a numeric score and display its status."""
    # score = float(input("Enter score: "))
    score = random.randint(0, 100)
    print(determine_status(score))


def determine_status(score: float):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
