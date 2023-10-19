from Test import test_creation_object
from Message import error_travel_creation


class Travel:
    TRAVEL_IN_PROGRESS = 0
    TRAVEL_DONE = 1
    TRAVEL_NOT_STARTED = 2

    def __init__(self, bus_route_depart: str, bus_route_arrive: str, departure_time: int):
        if test_creation_object([bus_route_depart, bus_route_arrive, departure_time]):
            raise Exception(error_travel_creation(bus_route_depart, bus_route_arrive, departure_time))
        self.bus_route_depart = bus_route_depart
        self.bus_route_arrive = bus_route_arrive
        self.departure_time = departure_time
        self.etat = self.TRAVEL_NOT_STARTED

    def get_bus_route_depart(self):
        return self.bus_route_depart

    def get_bus_route_arrive(self):
        return self.bus_route_arrive

    def get_departure_time(self):
        return self.departure_time

    def __str__(self):
        return f"Travel from {self.bus_route_depart} to {self.bus_route_arrive} at {self.departure_time}"

    def is_done(self):
        return self.etat == self.TRAVEL_DONE

    def is_in_travel(self):
        return self.etat == self.TRAVEL_IN_PROGRESS

    def is_not_started(self):
        return self.etat == self.TRAVEL_NOT_STARTED

    def set_etat(self, etat: int):
        self.etat = etat

    def get_etat(self):
        return self.etat
