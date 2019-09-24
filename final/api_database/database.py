import requests 
from .config import host
from exceptions.mileage_error import MileageError
from model.model import Vehicle

class VehicleDB():
        
    def insert(self, vehicle):
        try:
            print(vehicle)
            body = {'id': vehicle.id, 'vehicle': vehicle.name, 'total_miles': vehicle.miles }
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
            body = { 'id': vehicle.id, 'vehicle': vehicle.name, 'new_miles': new_miles }
            
            response = requests.patch(host + f'{vehicle.id}/increase_miles/', data = body)

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
        return [ Vehicle(v['vehicle'], v['total_miles'], v['id'] ) for v in response ]
        


db = VehicleDB()


# v1 = Vehicle('Zoe car ', 1000)
# v2 = Vehicle('Tilley car', 2000)
v1 = Vehicle('Zoe car ', 1000, 6)
v2 = Vehicle('Tilley car', 2000, 7)

# try:
#     db.insert(v1)
# except Exception as e:
#     print(e)

# try:
#     db.insert(v2)
# except Exception as e:
#     print(e)


try:
    db.increase_miles(v1, 20)
except Exception as e:
    print(e)

try:
    db.increase_miles(v2, 50)
except Exception as e:
    print(e)

print(db.get_all())
