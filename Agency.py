# from Administrator import *
from Administrators import *
from Flights import *
from Destinations import *


class Agency:
    def __init__(self):
        self.loggedInUser = None
        self.admins = Administrators()
        self.destinations = Destinations(self)
        self.flights = Flights(self)
        self.admins.insert_dummy_data()
        self.destinations.insert_dummy_data()

    def login(self, login_entry, pwd_entry):
        if self.admins.has_administrator(login_entry, pwd_entry):
            self.loggedInUser = self.admins.get_administrator(login_entry, pwd_entry)
            return self.loggedInUser


