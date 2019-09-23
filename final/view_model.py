# deal with view and repository

class ViewModel:

    def __init__(self, repo):
        # self.view = view
        self.repository = repo


    def insert(self, vehicle):
        self.repository.insert(vehicle)

    def add_miles(self, vehicle, miles):
        self.repository.update(vehicle, miles)

    def get_all_data(self):
        return self.repository.get_all_data()

    

