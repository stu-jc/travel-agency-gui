class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.logged_in_user = None

#login
    def login(self, log, pwd):
        self.logged_in_user = self.model.login(log, pwd)

#flights
    def view_all_flights(self):
        self.model.view_flights()

    def view_filtered_flights(self, string):
        return self.model.view_ff(string)

    def add_flight(self, airline, flightnum, takeoff, landing, cost):
        self.model.add_flight(airline, flightnum, takeoff, landing, cost)

    def remove_flight(self, takeoff, landing):
        self.model.remove_flight(takeoff, landing)

#destinations

    def view_filtered_destinations(self, string):
        return self.model.view_filtered_destinations(string)

    def add_destination(self, name, country):
        self.model.add_destination(name, country)

    def remove_destination(self, name, country):
        self.model.remove_destination(name, country)

#trips

    def add_connecting_flights(self):
        self.model.add_connecting_flights()

    def add_trip_destination(self, name, country):
        self.model.add_trip_destination(name, country)

    def remove_trip_destination(self, name, country):
        self.model.remove_trip_destination(name, country)

    def view_trip(self):
        return self.model.view_trip()

    def desti_or_flight(self, obj):
        return self.model.desti_or_flight(obj)

