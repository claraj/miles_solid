import sqlite3 

from model import *

class Vehicle():
    def __init__(self, name, miles=0):
        self.name = name 
        self.miles = miles 


    def __str__(self):
        return f'{self.name}, {self.miles} mile(s)'

    
class Car(Vehicle):
    pass


class Motorcycle(Vehicle):
    pass



