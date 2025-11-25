from datetime import datetime

from prac_09.wk9_prac_class import Person
from person import Person



class Student(Person):
    def __init__(self, student_id: int, course: str, **kwargs):
        #Person.__init__(self, name, birth_date)
        # self.name = name
        # self.birth_date =  birth_date
        super().__init__(**kwargs) # best approach for no repeating
        self.student_id = student_id
        self.course = course
        print("Student.init")

    def __repr__(self):
        return str(vars(self))
