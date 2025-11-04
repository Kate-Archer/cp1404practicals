"""
Prac 07
Read guitar csv file
Print a list of the give guitars sorted by year
"""
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

    # Print guitars from the list (oldest to newest based on year)
    for guitar in sorted(guitars):
        print(guitar)


main()