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
    name = str(input("Name:"))

    while name != "":
        try:
            year = int(input("Year:"))
            cost = float(input("Cost: $"))
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print(f"{name} ({year}) : ${cost: .2f} added.")
            name = str(input("Name:"))
        except ValueError:
            print("Year must be an integer (e.g. 2020). Cost must be a number.")
    print("...snip...")
    print("These are my guitars:")
    for index, new_guitar in enumerate(guitars, start=1):
        print(f"Guitar {index}: {new_guitar}")

#
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


main()