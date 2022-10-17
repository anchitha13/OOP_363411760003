"""
Name: {Anchitha Kutin}
SID: {363411760003}
Group: {MIT431}
"""

class Ev_Car:
    def __init__(self,brand,model,horsepower,batterySize,range,peice):
        self.brand = brand
        self.model = model
        self.horsepower = horsepower
        self.batterySize = batterySize
        self.range = range
        self.peice = peice

    def display_ev_car(self):
        print(f'display_ev_car name is {self.brand},{self.model},{self.horsepower},{self.batterySize},{self.range},{self.peice}')

