"""
Class ProgrammingLanguage
Time: 12:32 - 12:48 (first part) - 1:00 (last part)


"""

class ProgrammingLanguage:
    """Programming Language class."""
    def __init__(self, name = "", typing = "", reflection = "", year = 0):
        self.name = name.title()
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year


    def is_dynamic(self):
        """Determine if langauge is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string representation of the ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection = {self.reflection}, First appeared in {self.year}")

    def __repr__(self):
        """Reprint the data in the proper string format."""
        return str(self)


def run_tests():
    """Run a test on ProgrammingLanguage class with a small sample"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

# Prevent the run tests function from always running when importing
if __name__ == "__main__":
    run_tests()





