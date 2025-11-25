from wk9_prac_class import Person
from datetime import datetime
from student import Student

def main():
    p1 = Person("Joe", datetime(1995, 6, 15))
    p2 = Person("Jazzy", datetime(2000, 4, 13))
    print(p1)
    print(p2)
    print(p1.age())
    s1 = Student(name= "Jerry", birth_date= (2001, 12, 24), student_id= 12345, course= "EG1000")
    print(s1)
    print(s1.age())
main()
