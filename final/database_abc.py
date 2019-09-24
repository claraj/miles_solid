import abc 

class VehicleDB(abc.ABC):
    @abc.abstractmethod
    def insert(self, vehicle):
        pass


    @abc.abstractmethod
    def increase_miles(self, vehicle, new_miles):
        pass 


    @abc.abstractmethod
    def get_all(self):
        pass


    