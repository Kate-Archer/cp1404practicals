"""
cp1404
Extra practice questions
"""
import random


def main():
    number_of_scores = get_number_of_scores()
    random_scores = random.sample(range(0, 101), number_of_scores)
    print(random_scores)
    # The following for loop and file creator was found online and may not be the best method!
    with open("results.txt", "w") as out_file:
        for score in random_scores:
            status = determine_status(score)
            out_file.write(f"{score} is {status}\n")
            print(f"{score} is {status}")


def get_number_of_scores() -> int:
    """Collect and return the number of scores."""
    number_of_scores = int(input("How many scores are there?: "))
    while number_of_scores < 0:
        print("Cannot have a negative amount of scores!")
        number_of_scores = int(input("How many scores are there?: "))
    return number_of_scores


def determine_status(score):
    """Determine the status of a given random score."""
    if score not in range(0, 101):
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
