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

class Van(Vehicle):
    def __init__(self, name, seats, miles=0):
        super().__init__(name, miles)   # Call to superclass __init__ method
        self.seats = seats     # Set van-specific field 


class Motorcycle(Vehicle):
    def __init__(self, name, has_sidecar, miles=0):
        super().__init__(name, miles)   # Motorcycle-specific field 
        self.has_sidecar = has_sidecar




