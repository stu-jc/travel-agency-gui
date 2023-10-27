from Agency import Agency
from Flights import Flights
from Destinations import Destinations
from Destination import Destination


class Trip:
    def __init__(self, agency: Agency):
        self.agency = agency
        self.flights = Flights(self.agency)
        self.destinations = Destinations(self.agency)

    def trip_has_destination(self, name, country):
        for d in self.destinations.destinations:
            if d.name == name and d.country == country:
                return True
        return False

    def agency_has_destination(self, name, country):
        for d in self.agency.destinations.destinations:
            if d.name == name and d.country == country:
                return True
        return False

    def get_destination(self, name, country):
        for d in self.destinations.destinations:
            if d.name == name and d.country == country:
                return d
        return None

    def add_td(self, destination: Destination):
        if not self.agency_has_destination(destination.name, destination.country):
            raise Exception('THAT DONT EXIST IN THE AGENCY nigga')
        if self.trip_has_destination(destination.name, destination.country):
            raise Exception('YOU ALREADY ADDED THIS')
        else:
            self.destinations.destinations.append(destination)
            # print('\n NEW NEW NEW \n')
            # for d in self.destinations.destinations:
            #     print(d.name, d.country)

    def remove_td(self, destination: Destination):
        if not self.trip_has_destination(destination.name, destination.country):
            # # print('\n NEW NEW NEW \n')
            # for d in self.destinations.destinations:
            #     print(d.name, d.country)
            raise Exception('THAT DONT EXIST IN THE TRIPS U ADDED, nigga')
        else:
            self.destinations.destinations.remove(self.get_destination(destination.name, destination.country))
            # print('\n NEW NEW NEW \n')
            # for d in self.destinations.destinations:
                # print(d.name, d.country)

    def add_connecting_flights(self):
        if len(self.destinations.destinations) <= 1:
            # throw error
            raise Exception("Not enough destinations")
        self.flights.flights.clear()
        current_destination = None
        next_destination = None
        for i in range(len(self.destinations.destinations)):
            current_destination = self.destinations.destinations[i]
            if i == (len(self.destinations.destinations) - 1):
                return
            next_destination = self.destinations.destinations[i + 1]
            if current_destination == next_destination: #or current_destination.country == next_destination.country:
                #throw error
                raise Exception('Duplicate destinations i think')
            for f in self.agency.flights.flights:
                if f.takeoff == current_destination.country and f.landing == next_destination.country:
                    try:
                        self.flights.flights.append(f)
                    except:
                        #throw error
                        raise Exception('failure in trip line 33 add con flights')
                    break

    def get_itinery(self):
        objects = []
        for i in range(len(self.destinations.destinations)):
            objects.append(self.destinations.destinations[i])
            if i < len(self.flights.flights):
                objects.append(self.flights.flights[i])
        return objects
