"""
Project class
"""

class Project:
    """Construct Project class."""
    def __init__(self, name = "", start_date = "", priority = 0, cost_estimate = 0.0, completion_percent = 0):
        """Create Project class with given instances."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percent = completion_percent

    def __str__(self):
        """Return string representation of Project variables."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percent}% "


    def __repr__(self):
        """Reprint the data in the proper string format."""
        return str(self)

    def is_complete(self):
        """Check if the project is complete (100%) and return."""
        return self.completion_percent == 100

    def __lt__(self, other):
        """Sort project by highest priority."""
        return self.priority > other.priority

    def __lt__(self, other):
        """Sort project by date (ascending)."""
        return self.start_date < other.start_date

