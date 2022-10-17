"""
Name: {Anchitha Kutin}
SID: {363411760003
Group: {MIT431}
"""

class Teacher:
    def __init__(self,name):
        self.name = name
    def teacher_info(self):
        print(f'Teacher Name: {self.name}')

class Faculty:
    lst_teachar = list()
    def __init__(self,fac_name):
        self.fac.name = fac_name
    def fac_info(self):
        print(f'Faculty Name: {self.fac_name}')
    def add_teacher(self,Teacher):
        self.lst_teacher.append(Teacher)
    def teacher_info(self):
        print(f'In {self.fac_name} has teacher below:')
        for x in self.lst_teachar:
            x.teacher_info()

f1 = Faculty("MT")

t1 = Teacher("Puriwat")


