"""
Test the SilverServiceTaxi class.
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class."""
    # silver_taxi_1 = SilverServiceTaxi("Fancy taxi 1", 100, 20 )
    # print(silver_taxi_1)

    silver_taxi_2 = SilverServiceTaxi("Fancy taxi 2", 100, 2)

    assert silver_taxi_2.name == "Fancy taxi 2"
    assert silver_taxi_2.fuel == 100
    assert silver_taxi_2.fanciness == 2

    silver_taxi_2.drive(18)
    print(silver_taxi_2)
    print(f"fare is: {silver_taxi_2.get_fare()}")

if __name__ == "__main__":
    main()


