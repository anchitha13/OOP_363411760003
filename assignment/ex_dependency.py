"""
Name: {Anchitha Kutin}
SID: {363411760003
Group: {MIT431}
"""
from datetime import date
class Customer:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def customer_info(self):
        print(f'cusid: {self.id} cusname: {self.name}')

class Oder:
    def __init__(self,id,Customer,date,total_cost):
        self.id = id
        self.customer = Customer
        self.date = date
        self.total_cost = total_cost
    def oder_info(self):
        print(f'oder id: {self.id}'
              f'customer name: {self.customer.name}'
              f'date: {self.date}'
              f'totel cost: {self.total_cost}')

customer1 = Customer("cus001","Anchitha Kutin")

order1 = Oder("order001",customer1,date.today(),15000.00)

customer1.customer_info()
order1.oder_info()
