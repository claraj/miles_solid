"""User interface considerations only. Will pass all database queries to the ViewModel """

from .view_util import input_positive_float, show_vehicle_list, header
from model.model import Vehicle
from exceptions.mileage_error import MileageError


class View:

    def __init__(self, view_model):
        self.view_model = view_model


    def get_new_vehicles(self):

        header('Insert new vehicles into the database')

        while True:
            name = input('Enter new vehicle name to insert, or enter to quit: ')
            if not name:
                break

            miles = input_positive_float(f'Enter new miles driven for {name}: ')
            vehicle = Vehicle(name, miles)
            try:
                self.view_model.insert(vehicle)
            except MileageError as e:
                print(str(e))


    def update_existing_vehicles(self):

        header('Update miles for vehicles already in the database')

        while True:
            name = input('Enter existing vehicle name or enter to stop updating vehicles: ')
            if not name:
                break

            miles = input_positive_float(f'Enter new miles driven for {name}: ')
            
            vehicle = Vehicle(name)
            
            # Can substitute a Van for a Vehicle - code all still works, 
            # although DB would need to be updated to store the extra field. 
            
            # seats = int(input('Enter seats for van: '))
            # vehicle = Van(name, seats)
            
            try:
                self.view_model.increase_miles(vehicle, miles)
            except MileageError as e:
                print(str(e))


    def display_all_data(self):

        header('All vehicles in the database')

        all_vehicles = self.view_model.get_all()
        show_vehicle_list(all_vehicles)


