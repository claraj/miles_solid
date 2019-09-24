# Start view 

# High-level setup 

from view import * 

from sql_database.database import SQLVehicleDB     # Use this class to use the SQLite DB  
from api_database.database import APIVehicleDB     # Use this class to use the api DB  

from view.view import View 
from view_model import ViewModel

def main():

    vehicle_db = SQLVehicleDB()
    #vehicle_db = APIVehicleDB()    # Replace the SQLVehicleDB with this to use the API - code will be happy

    vehicle_view_model = ViewModel(vehicle_db)

    vehicle_view = View(vehicle_view_model)

    vehicle_view.get_new_vehicles()
    
    vehicle_view.update_existing_vehicles()

    vehicle_view.display_all_data()


if __name__ == '__main__':
    main()


