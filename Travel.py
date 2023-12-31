from Test import test_creation_object
from Message import error_travel_creation


class Travel:
    TRAVEL_IN_PROGRESS = 0
    TRAVEL_DONE = 1
    TRAVEL_NOT_STARTED = 2

    def __init__(self, bus_route_depart: str, bus_route_arrive: str, departure_time: int):
        if test_creation_object([bus_route_depart, bus_route_arrive, departure_time]):
            raise Exception(error_travel_creation(bus_route_depart, bus_route_arrive, departure_time))
        self._bus_route_depart = bus_route_depart
        self._bus_route_arrive = bus_route_arrive
        self._departure_time = departure_time
        self._etat = self.TRAVEL_NOT_STARTED

    def get_bus_route_depart(self):
        return self._bus_route_depart

    def get_bus_route_arrive(self):
        return self._bus_route_arrive

    def get_departure_time(self):
        return self._departure_time

    def __str__(self):
        etat = str(self._etat).replace("0", "In progress").replace("1", "Done").replace("2", "Not started")
        return f"Travel from {self._bus_route_depart} to {self._bus_route_arrive} at {self._departure_time} - etat: {etat}"

    def is_done(self):
        return self._etat == self.TRAVEL_DONE

    def is_in_travel(self):
        return self._etat == self.TRAVEL_IN_PROGRESS

    def is_not_started(self):
        return self._etat == self.TRAVEL_NOT_STARTED

    def set_etat(self, etat: int):
        self._etat = etat

    def get_etat(self):
        return self._etat
