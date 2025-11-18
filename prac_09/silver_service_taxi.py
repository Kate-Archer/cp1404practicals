"""
SilverServiceTaxi class.
"""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Silver Service taxi that inherits from a Taxi class."""

    # Extra charge for each new fare
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness: float):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """
        Get the current fare for the Silver service.
        This inherits from the Taxi class using get_fare
        and adding the flag fall for the Silver service.
        """
        return self.flagfall + super().get_fare()




