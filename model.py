from Agency import Agency
from Trip import Trip
from Flight import Flight
from Destination import Destination


class Model:
    def __init__(self):
        self.agency = Agency()
        self.trip = Trip(self.agency)

#login
    def login(self, login_entry, pwd_entry):
        try:
            self.agency.loggedInUser = self.agency.login(login_entry, pwd_entry)
            return self.agency.loggedInUser
        except:
            pass # make this throw error?

#flights
    def view_flights(self):
        for f in self.agency.flights.flights:
            print(f.get_airline(), f.get_flight_no(), f.get_takeoff(), f.get_landing(), f.get_cost())

    def view_ff(self, string):
        return self.agency.flights.get_filtered_flights(string)

    def add_flight(self, airline, flight_no, takeoff, landing, cost):
        try:
            airline = str(airline)
            flight_no = int(flight_no)
            takeoff = str(takeoff)
            landing = str(landing)
            cost = float(cost)

            flight_obj = Flight(airline, flight_no, takeoff, landing, cost)
            self.agency.flights.add_flight(flight_obj)
        except ValueError as e:
            raise Exception('Error occured ' + str(e))

    def remove_flight(self, takeoff, landing):
        takeoff = str(takeoff)
        landing = str(landing)
        self.agency.flights.remove_flight(takeoff, landing)

#destinations
    def view_filtered_destinations(self, string):
        return self.agency.destinations.get_destination_with_str(string)

    def add_destination(self, name, country):
        name = str(name)
        country = str(country)
        destination_obj = Destination(name, country)
        self.agency.destinations.add_destination(destination_obj)

    def remove_destination(self, name, country):
        name = str(name)
        country = str(country)
        destination_obj = Destination(name, country)
        self.agency.destinations.remove_trip_d(destination_obj)

    def add_trip_destination(self, name, country):
        name = str(name)
        country = str(country)
        destination_obj = Destination(name, country)
        self.trip.add_td(destination_obj)

    def remove_trip_destination(self, name, country):
        name = str(name)
        country = str(country)
        destination_obj = Destination(name, country)
        self.trip.remove_td(destination_obj)

    def add_connecting_flights(self):
        self.trip.add_connecting_flights()

    def view_trip(self):
        return self.trip.get_itinery()

    def desti_or_flight(self, obj):
      if isinstance(obj, Destination):
          return True
      # elif isinstance(obj, Flight):
      #     print('its a flight')
      else:
          return False
          # print('NOTHING')


















