"""Band Class"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a band with a name and empty instrument collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a band."""
        return f"{self.name} ({", ".join([musician.__str__() for musician in self.musicians])})"

    # def __repr__(self):
    #     """Return a string representation of a band, showing the variables."""
    #     return str(self)

    def add(self, musician):
        """Add a musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the band members."""
        if not self.musicians:
            return f"{self.name} has no musicians!"
        return "\n".join(musician.play() for musician in self.musicians)

# if __name__ == '__main__':
#
#     from guitar import Guitar
#
#     band = Band()
#     assert band.name == ""
#     assert band.instruments == []
#
#     band.name = "Lincoln Brewster"
#     band.instruments.append(Guitar("Fender Lincoln Brewster Stratocaster", 2020, 3419.0))
#     band.instruments.append(Guitar("Ernie Ball Music Man Silhouette Special", 1993, 2499.0))
#     print(band)
#     print(band.play())
