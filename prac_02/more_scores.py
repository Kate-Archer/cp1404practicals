import random


def main():
    number_of_scores = get_number_of_scores()
    random_scores = random.sample(range(0, 101), number_of_scores)
    print(random_scores)
    print(determine_status(random_scores))


def get_number_of_scores() -> int:
    number_of_scores = int(input("How many scores are there?: "))
    while number_of_scores < 0:
        print("Cannot have a negative amount of scores!")
        number_of_scores = int(input("How many scores are there?: "))
    return number_of_scores


def determine_status(random_scores):
    """Determine the status of a given random score."""
    # if random_scores != range(0, 101):
    #     return "Invalid score"
    if random_scores >= 90:
        return "Excellent"
    elif random_scores >= 50:
        return "Passable"
    else:
        return "Bad"

main()