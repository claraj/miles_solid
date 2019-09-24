import sqlite3 

from model import *

class Vehicle():
    def __init__(self, name, miles=0, id=None):
        self.name = name 
        self.miles = miles
        self.id = id


    def __str__(self):
        return f'{self.name}, {self.miles} mile(s)'


    def __repr__(self):
        return f'Name: {self.name}, Miles: {self.miles}'


class Car(Vehicle):
    pass


class Motorcycle(Vehicle):
    pass



