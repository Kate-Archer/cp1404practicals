"""
Guitar testing
Prac 06
"""
from prac_06.guitar import Guitar
def run_tests():
    """Test Guitar class for the year 2025."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    guitar = Guitar(name, year, cost)
    print(guitar)
    print(f"{guitar.get_age()}")
    print(f"{guitar.is_vintage()}")

    print(f"{guitar.name} get_age() - Expected 103, got {guitar.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected True, got {guitar.is_vintage()}")

    epic_guitar = Guitar("ケイト", 2015, 2000.00)
    print(f"{epic_guitar.name} get_age() - Expected 10, got {epic_guitar.get_age()}")
    print(f"{epic_guitar.name} is_vintage() - Expected False, got {epic_guitar.is_vintage()}")


if __name__ == '__main__':
    run_tests()

