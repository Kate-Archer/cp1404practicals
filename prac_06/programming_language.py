"""
Class ProgrammingLanguage
Time: 12:32 -


"""

class ProgrammingLanguage:
    """Programming Language class"""
    def __init__(self, language = "", typing = "", reflection = "", year = 0):
        self.language = language.title()
        self.typing = typing.title()
        self.reflection = reflection.title()
        self.year = year


    def is_dynamic(self):
        if self.typing.lower() == "dynamic":
            return True
        return None

    def __str__(self):
        return (f"{self.language}, {self.typing} Typing, "
                f"Reflection = {self.is_dynamic}, First appear in {self.year}")

    def __repr__(self):
        return str(self)




