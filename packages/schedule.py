import json

from packages.customers import Customer
from packages.professionals import Professional
from packages.database_manager import DatabaseManager

class Schedule(Customer, Professional):

    def __init__(self, db_path, name_customer=None, name_professional=None):
      self.name_customer = name_customer
      self.name_professional = name_professional
      self.__db_path = db_path
    
    def appointment(self):
        database = None
        if self.name_customer and self.name_professional in database:
            pass
        return False