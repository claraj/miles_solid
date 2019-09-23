# Start view 

# High-level setup 

from view import * 

from sql_database.database import VehicleDB     # Change this line to import the api DB instead 
from view.view import View 
from view_model import ViewModel
from repository import Repository 


def main():

    vehicle_db = VehicleDB()
    vehicle_repo = Repository(vehicle_db)
    vehicle_view_model = ViewModel(vehicle_repo)

    vehicle_view = View(vehicle_view_model)

    vehicle_view.get_new_vehicles()
    
    vehicle_view.update_existing_vehicles()

    vehicle_view.display_all_data()


if __name__ == '__main__':
    main()


