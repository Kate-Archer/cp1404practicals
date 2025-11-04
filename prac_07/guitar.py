"""
Prac 07 (modified)
Guitar Class
"""

class Guitar:
    def __init__(self, name = "", year = 0, cost = 0.0):
        """Create Guitar class with instances."""
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        """Sort guitars by year by defining which is less than the other (oldest to newest)."""
        return self.year < other.year

    def __str__(self):
        """Return string representation of Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __repr__(self):
        """Reprint the data in the proper string format."""
        return str(self)

    def get_age(self):
        """Return the age of the guitar based on the year it was purchased."""
        age = 2025 - self.year
        return age

    def is_vintage(self):
        """Check if the guitar is vintage (50 years old or more) and return."""
        return self.get_age() >= 50
