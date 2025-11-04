"""
Project class
"""

class Project:
    """Project class..."""
    def __init__(self, name = "", start_date = "", priority = 0, cost_estimate = 0.0, completion_percent = 0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percent = completion_percent

    def __str__(self):
        """Return string representation of Project variables."""
        #todo:
        return f"{self.name}, {self.start_date}, {self.priority}"

    def __repr__(self):
        """Reprint the data in the proper string format."""
        return str(self)

