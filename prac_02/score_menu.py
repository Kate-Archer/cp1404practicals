""""
CP1404 - Practical
Make a menu with four options
Get a valid score (0-100)
Print result (copy or import function to determine result from score.py)
Show stars (print as many stars as the score)
Quit
"""
MENU = """ G - Get a valid score (0-100)\n P - Print result (grade)\n S - Show stars equivalent to score\n Q - Quit"""


def main():
    """Get a valid score."""
    score = get_valid_score()

    """Show MENU options."""

    print(MENU)
    choice = input(">>> ").upper()
    """="""
    while choice != "Q":
        if choice == "G":
            print(score)
        elif choice == "P":
            print(determine_status(score))
        elif choice == "S":
            print_asterisks(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you. Goodbye!")


def get_valid_score() -> float:
    """Return valid score for the menu."""
    score = float(input("What is your score?: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("What is your score?: "))
    return score


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


def print_asterisks(score):
    """Print an amount of asterisks equivalent to the score amount (rounded)."""
    for i in range(int(score)):
        print('*', end=' ')
        # Allow a new line after every 20th asteriskA
        if i % 20 == 0:
            print()
    print()


main()
