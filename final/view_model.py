# deal with view and repository

class ViewModel:

    def __init__(self, db):
        self.db = db

    def insert(self, vehicle):
        self.db.insert(vehicle)

    def increase_miles(self, vehicle, miles):
        self.db.increase_miles(vehicle, miles)

    def get_all(self):
        return self.db.get_all()

    

