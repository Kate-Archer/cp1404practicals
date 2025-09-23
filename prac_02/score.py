"""
CP1404/CP5632 - Practical 1
Program to determine score status
Fixed to determine score status, with function
"""
import random


def main():
    """ Get a numeric score and display its status """
    # score = float(input("Enter score: "))
    score = random.randint(0, 100)
    print(determine_status(score))


def determine_status(score: float):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
