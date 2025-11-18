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



