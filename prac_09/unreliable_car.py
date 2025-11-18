"""
UnreliableCar class inherits from Car class
UnreliableCar contains reliability
"""
from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Unreliable car that inherits from the Car class."""
    def __init__(self, name, fuel, reliability=0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Drive UnreliableCar like parent Car but
        only if the randomly generated distance (0-100)
        is less than the car's reliability.
        """
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0 # Distance not driven
        distance_driven = super().drive(distance)
        return distance_driven



