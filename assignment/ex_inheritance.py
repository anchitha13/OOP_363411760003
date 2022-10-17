"""
Name: {Anchitha Kutin}
SID: {363411760003
Group: {MIT431}
"""

class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def person_info(self):
        print(f'Name: {self.name} Age: {self.age}')

class Student(Person):
    def __init__(self,name,age,major,gpa):
        Person.__init__(self, name, age)

        self.major = major
        self.gpa = gpa
def student_info(self):
    print(f'Name: {self.name} Age: {self.age}'
          f'Major: {self.major}'
          f'GPA: {self.gpa}')

s1 = Student("Anchitha Kutin",21,"MIT",3.00)
s1.person_info()



