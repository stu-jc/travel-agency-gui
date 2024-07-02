from Destination import Destination
from Utils import Utils


class Destinations:
    def __init__(self, agency):
        self.agency = agency
        self.destinations = []
    
    def add_destination(self, destination: Destination):
        if self.has_destination(destination.name, destination.country):
            #throw error
            raise Exception('We already have this destination')
        else:
            self.destinations.append(destination)
            Utils.add_flights_for_destination(self.destinations[-1], self.agency)

    def remove_destination(self, destination: Destination):
        if not self.has_destination(destination.name, destination.country):
            #throw error
            raise Exception('destination does not EXIST ')
        else:
            self.destinations.remove(self.get_destination(destination.name, destination.country))
    
    def has_destination(self, name, country):
        for d in self.destinations:
            if d.name == name and d.country == country:
                return True
        return False
    
    def get_destination(self, name, country):
        if not self.has_destination(name, country):
            #throw error
            pass
        for d in self.destinations:
            if d.name == name and d.country == country:
                return d
        return None

    def get_destination_with_str(self, string):
        destis = []
        for d in self.destinations:
            if string.lower() in d.name.lower() or string.lower() in d.country.lower():
                destis.append(d)
        return destis

    def call_add_flights(self):
        from Utils import Utils
        for d in self.destinations:
            Utils.add_flights_for_destination(d, self.agency)

    def insert_dummy_data(self):
        self.destinations.append(Destination("Eiffel Tower", "France"))
        self.destinations.append(Destination("Opera House", "Australia"))
        self.destinations.append(Destination("Uluru", "Australia"))
        self.destinations.append(Destination("Machu Picchu", "Peru"))
        self.destinations.append(Destination("Great Pyramids", "Egypt"))
        self.destinations.append(Destination("Niagara Falls", "Canada"))
        self.call_add_flights()


    
    
