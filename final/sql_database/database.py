import sqlite3 
# from .config import db  # .config means import from this directory 
from .config import db_path
from exceptions.mileage_error import MileageError
from database_abc import VehicleDB
from model.model import Vehicle
from utils.validation import ensure_positive_float

db = db_path

class SQLVehicleDB(VehicleDB):

    def __init__(self):
        with sqlite3.connect(db) as con:
            con.execute('CREATE TABLE IF NOT EXISTS MILES (vehicle TEXT UNIQUE NOT NULL, total_miles FLOAT)')
        

    def insert(self, vehicle):

        miles = ensure_positive_float(vehicle.miles)
        if miles is None:
            raise MileageError('Miles must be a positive number')

        try:
            with sqlite3.connect(db) as con:
                rows_mod = con.execute('INSERT INTO MILES VALUES (?, ?)', (vehicle.name, miles))
            con.close()
            return rows_mod
        except sqlite3.IntegrityError as ie:
            raise MileageError(f'Error inserting: will not add duplicate vehicle with name {vehicle.name}')    # duplicate vehicle 


    def increase_miles(self, vehicle, new_miles):

        miles = ensure_positive_float(new_miles)
        if miles is None:
            raise MileageError('Miles must be a positive number')

        with sqlite3.connect(db) as con:
            cursor = con.execute('UPDATE MILES SET total_miles = total_miles + ? WHERE vehicle = ?', (miles, vehicle.name))
            rows_mod = cursor.rowcount
        con.close()
        
        if rows_mod == 0:
            raise MileageError(f'Error updating: Vehicle {vehicle.name} not found')
     

    def get_all(self):
        con = sqlite3.connect(db) 
        vehicles_cursor = con.execute('SELECT * FROM MILES')
        vehicles = [ Vehicle(*row) for row in vehicles_cursor.fetchall() ]
        con.close()
        return vehicles
