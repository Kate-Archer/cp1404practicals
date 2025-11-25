"""
Test the Unreliable Car test several times
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test unreliable cars with varying reliabiltiies and distances """
    old_car = UnreliableCar("Old car", 100, 20)
    new_car = UnreliableCar("New car", 130, 95)

    # Attempt to drive the cars several times
    # Print the distance they successfully drove
    for i in range(1, 15):
        print(f"Try to drive the car {i}km: ")
        print(f"The {old_car.name} can drive {old_car.drive(i)}km")
        print(f"The {new_car.name} can drive {new_car.drive(i)}km")
        print(f"-------------------------") # Split the iterations up clearly

    # The final state of the cars
    print(old_car)
    print(new_car)


main()