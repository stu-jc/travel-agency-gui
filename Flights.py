from Flight import Flight


class Flights:
    def __init__(self, agency):
        # self.agency = agency
        self.flights = []
    
    def add_flight(self, flight: Flight):
        if self.has_flight(flight.takeoff, flight.landing):
            #throw error
            raise Exception('We already have this flight NIGGA')
        else:
            self.flights.append(flight)

    def remove_flight(self, takeoff, landing):
        if not self.has_flight(takeoff, landing):
            #throw error
            raise Exception('Flight does not exist NIGGA')
        else:
            self.flights.remove(self.get_flight(takeoff, landing))
    
    def has_flight(self, takeoff, landing):
        for f in self.flights:
            if f.takeoff == takeoff and f.landing == landing:
                return True
        return False
    
    def get_flight(self, takeoff, landing):
        for f in self.flights:
            if f.takeoff == takeoff and f.landing == landing:
                return f
        return None
    
    def get_filtered_flights(self, string):
        filtered = []
        for f in self.flights:
            if string.lower() in f.takeoff.lower() or string.lower() in f.landing.lower():
                filtered.append(f)
        return filtered
    
    def get_total_cost(self):
        cost = 0.0
        for f in self.flights:
            cost = cost + f.cost
        return cost
