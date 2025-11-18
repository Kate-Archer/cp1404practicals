"""
Test first taxi using the Taxi and Car class functions
"""
from prac_09.taxi import Taxi


def main():
    """Test the Taxi class."""

    my_taxi = Taxi("Pruis 1", 100)
    my_taxi.drive(40)  # Drive 40km
    print(my_taxi)

    my_taxi.start_fare()  # Reset fare to 0
    print(my_taxi)

    my_taxi.drive(100)  # Drive 100km
    print(my_taxi)


main()
