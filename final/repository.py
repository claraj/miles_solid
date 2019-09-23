"""

Repository.py

Pass messages from viewmodel to database 

"""

class Repository:

    def __init__(self, db):

        self.db = db

    def insert(self, vehicle):
        return self.db.insert(vehicle)


    def update(self, vehicle, new_miles):
        return self.db.increase_miles(vehicle, new_miles)


    def get_all_data(self):
        return self.db.get_all()