from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Silver Service taxi that inherits from a Taxi class."""

    Taxi.price_per_km

    def __init__(self, name, fuel, fanciness: float):
        super().__init__(name, fuel)
        self.fanciness = fanciness

    def get_price_per_km(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.fanciness


    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven




