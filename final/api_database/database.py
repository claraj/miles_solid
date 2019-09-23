import requests 
from config import base_url

class MileageError(Exception):
    pass


class VehicleDB():

    def __init__(self, db):
        self.db = db 

        
    def insert(self, vehicle)
        try:
            response = requests.post(base_url, vehicle)
            if response.status_code == 201:
                return 
            else: 
                # check error message and raise specific error 
                raise MileageError('duplicate vehicle')    
        except:
            

    def increase_miles(self, vehicle, miles):
        
        try:
            response = requests.post(base_url, vehicle)
            if response.status_code == 201:
                return 
            else: 
                # check error message and raise specific error 
                raise MileageError('vehicle not found')    
        except:

    def get_all(self):
        requests.get()
        