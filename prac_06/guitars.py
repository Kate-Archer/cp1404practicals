"""
Add a list of guitars
prac 06
Time: 1:56 - 2:40 (took breaks)
"""
from prac_06.guitar import Guitar


def main():
    """Guitar list (Guitar class)."""
    guitars = []

    print("My guitars!")
    name = str(input("Name:")).title()

    while name != "":
        year = handle_year_exception()
        cost = handle_cost_exception()

        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{name} ({year}) : ${cost: .2f} added.")
        name = str(input("Name:"))

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars: # Handle the ValueError when no guitars are given.
        print("...snip...")
        print("These are my guitars:")

        max_name, max_year, max_cost = compute_max_lengths(guitars)
        for index, new_guitar in enumerate(guitars, start=1):
            vintage_string = ""
            if new_guitar.is_vintage():
                vintage_string = "(vintage)"
            print(f"Guitar {index}: {new_guitar.name:>{max_name}} ({new_guitar.year:>{max_year}}), worth ${new_guitar.cost: >{max_cost}} {vintage_string}")
    else:
        print("Theres no guitars :<, buy one!")

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



def compute_max_lengths(guitars):
    """Compute the maximum column lengths for the guitar details (name, year, cost)."""
    max_name = max(len(guitar.name) for guitar in guitars)
    max_year = max(len(str(guitar.year)) for guitar in guitars)
    max_cost = max(len(f"{guitar.cost:.2f}") for guitar in guitars)
    return max_name, max_year, max_cost

main()