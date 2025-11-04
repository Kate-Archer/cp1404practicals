"""
Prac 07
Read guitar csv file
Print a list of the given guitars (and added) sorted by year
"""
from prac_07.guitar import Guitar


def main():
    """Read file of programming guitar details (name, year, cost), save as objects and display in a list."""
    guitar, guitars = load_guitars()

    # Add a new guitar (name, year, cost)
    print("My guitars!")
    name = str(input("Name:")).title()

    while name != "":
        year = get_valid_year()
        cost = get_valid_cost()
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{name} ({year}) : ${cost: .2f} added.")
        name = str(input("Name:"))

    # Add the new guitar to the file
    update_guitars(guitars)

    # Print guitars from the list (oldest to newest based on year)
    if guitars:  # Handle the ValueError when no guitars are given.
        print("These are my guitars:")
        for guitar in sorted(guitars):
            print(guitar)
    else:
        print("There are no guitars :<, buy one!")


def load_guitars():
    """Load the guitar.csv file and split it into the necessary parts (name, year, cost)."""
    guitars = []
    try:
        in_file = open('guitars.csv', 'r')
        in_file.readline()  # Skip reading the header
        for line in in_file:
            parts = line.strip().split(',')
            # Construct a guitar object using the elements
            name = parts[0]
            year = parts[1]
            cost = parts[2]
            guitar = Guitar(name, year, cost)
            # Add the new guitar to the list
            guitars.append(guitar)
        # Close the file after reading it
        in_file.close()
    except FileNotFoundError:
        print("The csv file chosen cannot be found")

    return guitar, guitars


def update_guitars(guitars):
    """Update the guitar.csv to include the new guitars added."""
    try:
        with open("guitars.csv", "w", newline="") as out_file:
            out_file.write("Name,Year,Cost\n")
            for guitar in guitars:
                out_file.write(f"{guitar.name},{int(guitar.year)},{float(guitar.cost):.2f}\n")

    except FileNotFoundError:
        print("The csv file chosen cannot be found")


def get_valid_cost():
    """Handle cost exceptions (non float or non integer input)."""
    while True:
        try:
            cost = float(input("Cost: $"))
            return cost
        except ValueError:
            print("Cost must be a number.")


def get_valid_year():
    """Handle year exceptions (non integer input)."""
    while True:
        try:
            year = int(input("Year:"))
            return year
        except ValueError:
            print("Year must be an integer (e.g. 2020).")


main()
