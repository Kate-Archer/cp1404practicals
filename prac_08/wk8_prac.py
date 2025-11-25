"""
-
"""


class Product:
    """Class Product."""

    def __init__(self, name="", price=0.0):
        """Construct a Product class from the given values (name and price)."""
        self.name = name
        self.price = price

    def __str__(self):
        """Return string representation of the Product."""
        return f"{self.name.title()}, ${self.price: .2f}."
