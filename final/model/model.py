"""
Model objects, represent entities in the program, and data in the data store. 
"""

class Vehicle():
    def __init__(self, name, miles=0):
        self.name = name 
        self.miles = miles


    def __str__(self):
        return f'{self.name}, {self.miles} mile(s)'


    def __repr__(self):
        return f'Name: {self.name}, Miles: {self.miles}'



# Can make Car and Van and Motorcycle subclasses and everything still works 
class Car(Vehicle):
    pass


class Motorcycle(Vehicle):
    pass



