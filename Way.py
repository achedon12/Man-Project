from Test import test_creation_object
from Message import *


class Way:

    def __init__(self, number: int, departure: str, arrival: str, time: int):
        if test_creation_object([departure, arrival, time]):
            raise Exception(error_route_creation(departure, arrival, time))
        self.number = number
        self.departure = departure
        self.arrival = arrival
        self.time = time

    def get_route(self):
        return self.departure + self.arrival

    def get_time(self):
        return self.time

    def get_route_number(self):
        return self.number
