import requests 
from .config import host
from exceptions.mileage_error import MileageError
from model.model import Vehicle

class VehicleDB():
        
    def insert(self, vehicle):
        try:
            print(vehicle)
            body = {'vehicle': vehicle.name, 'total_miles': vehicle.miles }
            response = requests.post(host, data = body)
            if response.status_code == 201:
                return 
            else: 
                # check error message and raise specific error 
                raise MileageError('duplicate vehicle')    
        except Exception as e:
            print('Error inserting because ' + str(e))
            raise e
            

    def increase_miles(self, vehicle, new_miles):
        
        try:
            body = { 'vehicle': vehicle.name, 'new_miles': new_miles }
            
            response = requests.patch(host + f'{vehicle.name}/increase_miles/', data = body)

            if response.status_code == 201:
                return   # success 
            if response.status_code == 404: 
                raise MileageError('vehicle not found')    
      
        except Exception as e:
            print('Error increasing miles because ' + str(e))
            raise e 


    def get_all(self):
        response = requests.get(host).json()
        print( response)
        return [ Vehicle(v['vehicle'], v['total_miles'] ) for v in response ]
        

