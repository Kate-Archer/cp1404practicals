"""
Prac 07
Read guitar csv file
Print a list of the give guitars sorted by year
"""
from prac_03.capitalist_conrad import out_file
from prac_07.guitar import Guitar


def main():
    """Read file of programming guitar details (name, year, cost), save as objects and display in a list."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline() # Skip reading the header
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

    # Add a new guitar (name, year, cost)
    print("My guitars!")
    name = str(input("Name:")).title()

    while name != "":
        year = handle_year_exception()
        cost = handle_cost_exception()
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{name} ({year}) : ${cost: .2f} added.")
        name = str(input("Name:"))

    # Add the new guitar to the file
    with open("guitars.csv", "w") as out_file:
        print(guitar), out_file


    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


    # Print guitars from the list (oldest to newest based on year)
    if guitars:  # Handle the ValueError when no guitars are given.
        print("...snip...")
        print("These are my guitars:")
        for guitar in sorted(guitars):
            print(guitar)
    else:
        print("There are no guitars :<, buy one!")


def handle_cost_exception():
    """Handle cost exceptions (non float or non integer input)."""
    while True:
        try:
            cost = float(input("Cost: $"))
            return cost
        except ValueError:
            print("Cost must be a number.")


def handle_year_exception():
    """Handle year exceptions (non integer input)."""
    while True:
        try:
            year = int(input("Year:"))
            return year
        except ValueError:
            print("Year must be an integer (e.g. 2020).")




main()