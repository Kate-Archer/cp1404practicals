"""
Taxi simulator
"""

from prac_09.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """
    Run a taxi simulator that lets the user choose taxis,
    drive trips (a certain distance), and accumulate the total bill.
    """

    # Default values
    total_bill = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = input(">>> ").lower()  # Set the input to lowercase
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            current_taxi = choose_valid_taxi(current_taxi, taxis)

        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                drive_taxi(current_taxi)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive!")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def drive_taxi(current_taxi: Taxi | SilverServiceTaxi):
    """Drive a taxi a given distance (updates odometer)."""
    distance_to_drive = float(input("Drive how far?: "))
    current_taxi.drive(distance_to_drive)


def choose_valid_taxi(current_taxi: Taxi | SilverServiceTaxi, taxis: list[Taxi | SilverServiceTaxi]) -> Taxi | SilverServiceTaxi:
    """Choose a valid taxi from the list/index."""
    try:
        taxi_choice = int(input("Choose a taxi: "))
        current_taxi = taxis[taxi_choice]
    except ValueError:
        print("Invalid input - please enter a number.")
    except IndexError:
        print("Invalid taxi choice - no taxi under that number.")
    return current_taxi


def display_taxis(taxis):
    """Display numbered index list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def test_classes():
    """Test the Car and Taxi classes, and see if they work."""
    tesla = Car("Tesla", 200)
    tesla.drive(40)
    print(vars(tesla))
    assert tesla.fuel == 200
    assert tesla.odometer == 40
    tesla.drive(64)
    print(tesla)

    distance = int(input("Drive how far?: "))
    while distance > 0:
        distance_travelled = tesla.drive(distance)
        print(f"{tesla} travelled {distance_travelled}")
        distance = int(input("Drive how far?: "))

    taxi_test = Taxi("Prius 1", 100)
    print(taxi_test)
    taxi_test.drive(25)
    print(taxi_test, taxi_test.get_fare())
    taxi_test.start_fare()
    taxi_test.drive(40)
    print(taxi_test, taxi_test.get_fare())

    silver_taxi_test = SilverServiceTaxi("Limo", 100, 2)
    assert silver_taxi_test.fuel == 100
    assert silver_taxi_test.fanciness == 2
    print(silver_taxi_test, silver_taxi_test.get_fare())
    silver_taxi_test.drive(10)
    print(silver_taxi_test, silver_taxi_test.get_fare())


# test_classes()
main()
