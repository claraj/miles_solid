import sqlite3 
from .config import db  # Import from this directory 
from exceptions.mileage_error import MileageError
from model.model import Vehicle

class VehicleDB():

    def __init__(self):
        with sqlite3.connect(db) as con:
            con.execute('CREATE TABLE IF NOT EXISTS MILES (vehicle TEXT UNIQUE NOT NULL, total_miles FLOAT)')
        

    def insert(self, vehicle):
        try:
            with sqlite3.connect(db) as con:
                rows_mod = con.execute('INSERT INTO MILES VALUES (?, ?)', (vehicle.name, vehicle.miles))
            con.close()
            return rows_mod
        except sqlite3.IntegrityError as ie:
            raise MileageError(f'Error inserting: will not add duplicate vehicle with name {vehicle.name}')    # duplicate vehicle 


    def increase_miles(self, vehicle, new_miles):

        with sqlite3.connect(db) as con:
            cursor = con.execute('UPDATE MILES SET total_miles = total_miles + ? WHERE vehicle = ?', (vehicle.name, new_miles))
            rows_mod = cursor.rowcount
        con.close()
        
        if rows_mod == 0:
            raise MileageError(f'Error updating: Vehicle {vehicle.name} not found')
     

    def get_all(self):
        con = sqlite3.connect(db) 
        vehicles_cursor = con.execute('SELECT rowid, * FROM MILES')
        vehicles = [ Vehicle(*row) for row in vehicles_cursor.fetchall() ]
        con.close()
        return vehicles
