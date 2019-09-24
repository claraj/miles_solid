import requests 
from .config import host
from exceptions.mileage_error import MileageError
from database_abc import VehicleDB
from model.model import Vehicle

""" Connects to server and makes API calls.
Implements the same interface as the sql_database version of VehicleDB
"""


class APIVehicleDB(VehicleDB):
        
    def insert(self, vehicle):
        try:
            print(vehicle)
            body = {'vehicle': vehicle.name, 'total_miles': vehicle.miles }
            response = requests.post(host, data = body)
            if response.status_code == 201:
                return 
            else: 
                errors = response.json()['vehicle']
                # check error message and raise specific error 
                raise MileageError('Error inserting new vehicle because ' + ', '.join(errors))    
        except Exception as e:
            raise e
            

    def increase_miles(self, vehicle, new_miles):
        
        try:
            body = { 'vehicle': vehicle.name, 'new_miles': new_miles }
            response = requests.patch(host + f'{vehicle.name}/increase_miles/', data = body)

            if response.status_code == 201:
                return   # success 
            if response.status_code == 404: 
                raise MileageError(f'Vehicle {vehicle.name} not found')    
        except Exception as e:
            raise e 


    def get_all(self):
        response = requests.get(host).json()
        return [ Vehicle(v['vehicle'], v['total_miles'] ) for v in response ]
        

