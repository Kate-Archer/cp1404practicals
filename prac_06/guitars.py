"""
Add a list of guitars
prac 06
1:56 -
"""
from prac_06.guitar import Guitar


def main():
    """eee"""
    guitars = []
    name = str(input("Name:"))


    while name != "":
        year = int(input("Year:"))
        cost = float(input("Cost:"))
        print(f"{name} ({year}) : ${cost: .2f} added.")
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
    print("These are my guitars:")
    for index, (name, year, cost) in enumerate(guitars, start=1):
        for guitar in guitars:
            print(f"Guitar {index}: {guitar}")





main()