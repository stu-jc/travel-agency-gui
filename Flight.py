class Flight:
    def __init__(self, airline: object, flight_no: object, takeoff: object, landing: object, cost: object):
        self.airline = str(airline)
        self.flight_no = int(flight_no)
        self.takeoff = str(takeoff)
        self.landing = str(landing)
        self.cost = format(cost, '.2f')
    
    def get_airline(self):
        return self.airline

    def get_flight_no(self):
        return self.flight_no

    def get_takeoff(self):
        return self.takeoff

    def get_landing(self):
        return self.landing

    def get_cost(self):
        return self.cost
