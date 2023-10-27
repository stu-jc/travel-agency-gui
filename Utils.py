import random
from Destination import Destination
import Agency
from Flight import Flight #this was not here before, I have manually added this


class Utils:
    flight = Flight
    @staticmethod
    def add_flights_for_destination(destination: Destination, agency: Agency): #its a static method so it does not need self, that was breaking it
        country = destination.country
        airlines = ["American Airlines", "QANTAS", "JetStar", "Tiger Airways", "United Airlines", "Egypt Air", "Etihad", "Singapore Airlines", "British Air", "Cathay Dragon"]
        flight_min = 11
        flight_max = 999

        cost_min = 49.99
        cost_max = 999.99

        countries = []
        for d in agency.destinations.destinations:
            countries.append(d.country)
        
        for s in countries:
            try:
                # 4 factorial flights (24) minus flights from country to country = 20 flights total
                if s == country:  #needed to be added so that flights to each country don't happen
                    continue
                flight_obj_1 = Flight(airlines[random.randint(0, (len(airlines) - 1))], random.randint(int(flight_min), int(flight_max)), country, s, random.uniform(cost_min, cost_max))
                flight_obj_2 = Flight(airlines[random.randint(0, (len(airlines) - 1))], random.randint(int(flight_min), int(flight_max)), s, country, random.uniform(cost_min, cost_max))
                if not agency.flights.has_flight(flight_obj_1.takeoff, flight_obj_1.landing):
                    agency.flights.add_flight(flight_obj_1)
                if not agency.flights.has_flight(flight_obj_2.takeoff, flight_obj_2.landing):
                    agency.flights.add_flight(flight_obj_2)

            except:
                print('utils method failed for: ' + 's: ' + str(s) + ' country: ' + str(country)) # i added this too
                continue
