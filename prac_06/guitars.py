"""
Add a list of guitars
prac 06
1:56 -
"""
from prac_06.guitar import Guitar


def main():
    """eee"""
    guitars = []

    print("My guitars!")
    name = str(input("Name:")).title()

    while name != "":
        try:
            year = int(input("Year:"))

        except ValueError:
            print("Year must be an integer (e.g. 2020).")
            continue
        try:
            cost = float(input("Cost: $"))
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print(f"{name} ({year}) : ${cost: .2f} added.")
            name = str(input("Name:"))
        except ValueError:
            print("Cost must be a number.")
            continue

    print("...snip...")
    print("These are my guitars:")

    max_name, max_year, max_cost = compute_max_lengths(guitars)
    for index, new_guitar in enumerate(guitars, start=1):
        vintage_string = ""
        if new_guitar.is_vintage():
            vintage_string = "(vintage)"
        print(f"Guitar {index}: {new_guitar.name:>{max_name}} ({new_guitar.year:>4}), worth ${new_guitar.cost:>{max_year}}{vintage_string}")

#
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

def compute_max_lengths(guitars):
    """Compute the maximum column lengths for the guitar details (name, year, cost)."""
    max_name = max(len(guitar.name) for guitar in guitars)
    max_year = max(len(str(guitar.year)) for guitar in guitars)
    max_cost = max(len(f"{guitar.cost:.2f}") for guitar in guitars)
    return max_name, max_year, max_cost

main()