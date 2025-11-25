from datetime import datetime



class Person:
    def __init__(self, name: str, birth_date: datetime.date):
        self.name = name
        self.birth_date = birth_date
        print("Person.init")


    def __repr__(self):
        date_string = datetime.strftime(self.birth_date, "%d/%m/%Y")
        return f"Name: {self.name},  Birthdate: {date_string}"

    def age(self):
        return int((datetime.now() - self.birth_date).days / 365.2425)

if __name__ == '__main__':
    p0 = Person("Jane", datetime(1999, 2, 14))
    print(p0)
    print(p0.name)
    print(p0.age())