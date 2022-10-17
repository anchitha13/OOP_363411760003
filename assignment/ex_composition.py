"""
Name: {Anchitha Kutin}
SID: {363411760003
Group: {MIT431}
"""

class Faculty:
    def __init__(self,fac_name):
        self.fac_name = fac_name
    def fac_info(self):
        print(f'Faculty Name: {self.fac_name}')

class University:
    lst_faculty = list()

    def __init__(self,uniname):
        self.uniname = uniname
    def uni_info(self):
        print(f'University name: {self. uniname}')

    def get_faculty(self):
        f1 = Faculty("MT")
        f2 = Faculty("Sci")
        self.lst_faculty.append(f1)
        self.lst_faculty.append(f2)
    def fac_into(self):
        print(f"This {self.uniname} has faculty below")
        for x in self.lst_faculty:
            x.fac_info()

u1 =  University("RUTS")
u1.get_faculty()

u1.uni_info()
u1.fac_into()
