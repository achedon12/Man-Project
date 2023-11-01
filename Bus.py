from Message import *
from Person import Person
from Test import test_creation_object


def init():
    bus1 = Bus(1, 10, 1, 30, 'bus', 'BACECA')
    bus2 = Bus(2, 10, 1, 30, 'bus', 'DCEC')
    bus3 = Bus(3, 10, 1, 30, 'bus', 'BED')
    bus4 = Bus(4, 2, 1, 10, 'bus', 'AC')
    return [bus1, bus2, bus3, bus4]


class Bus:

    def __init__(self, bus_number: int, max_passengers: int, charge_speed: int, travel_speed: int|float, type: str,
                 route: str = ""):
        if test_creation_object([bus_number, max_passengers, charge_speed, travel_speed, route]):
            raise Exception(error_bus_creation(bus_number))
        self._time = 0
        self._bus_number = bus_number
        self._charge_speed = charge_speed
        self._travel_speed = travel_speed
        self._route = route
        self._passengers = []
        if route != "":
            self._current_station = self._route[0]
        else:
            self._current_station = ""
        self._max_passengers = max_passengers
        self._is_charge = False
        self._is_decharge = False
        self._history = ""
        self._direct = False
        self.type = type

        # True = going to the end of the route
        self._etat = False

    def __str__(self):
        return f"Bus {self._bus_number} is at station {self._current_station} with {len(self._passengers)} passengers"

    def get_passengers(self):
        return self._passengers

    def get_current_station(self):
        return self._current_station

    def get_bus_number(self):
        return self._bus_number

    def get_charge_speed(self):
        return self._charge_speed

    def get_travel_speed(self):
        return self._travel_speed

    def get_route(self):
        return self._route

    def set_route(self, route: str):
        self._route = route

    def add_passenger(self, passenger):
        self._passengers.append(passenger)

    def remove_passenger(self, passenger: Person):
        self._passengers.remove(passenger)

    def move_station(self):
        self._history += self._current_station
        if self.is_direct():
            next_station = self.update_station_direct()
            self._current_station = next_station
        else:
            self._current_station = self.get_next_station()

    def get_next_station(self):
        if self.is_direct():
            direct_route = self.get_direct()
            return direct_route[0]
        else:
            if self._current_station not in self._route:
                index = self._route.index(self.get_current_station_from_history())
            else:
                index = self._route.index(self._current_station)
            if index == self.get_end_route_index():
                return self._route[index - 1]
            if self._etat:
                return self._route[index - 1]
            return self._route[index + 1]

    def get_current_station_from_history(self):
        history = self._history
        history = history[-1]
        while len(history) > 0:
            potential_station = history[-1]
            if potential_station not in self.get_route():
                history = history[:-1]
            else:
                return potential_station

    def get_previous_station(self):
        index = self._route.index(self._current_station)
        if self._etat:
            return self._route[index + 1]
        return self._route[index - 1]

    def get_previous_station_from_history(self):
        if self._history == "":
            return self._current_station
        return self._history[-1]

    def get_max_passengers(self):
        return self._max_passengers

    def get_etat(self):
        return self._etat

    def change_etat(self):
        self._etat = not self._etat
        return self._etat

    def can_charge(self):
        return self._etat

    def get_end_route(self):
        return self._route[-1]

    def get_start_route(self):
        return self._route[0]

    def get_end_route_index(self):
        return len(self._route) - 1

    def get_current_station_index(self):
        if self.is_direct():
            return -1
        return self._route.index(self._current_station)

    def is_full(self):
        return len(self._passengers) >= self._max_passengers

    def is_empty(self):
        return len(self._passengers) == 0

    def get_available_seats(self):
        return self._max_passengers - len(self._passengers)

    def get_charge_time(self):
        return self._max_passengers * self._charge_speed

    def get_travel_time(self):
        return len(self._route) * self._travel_speed

    def get_total_time(self):
        return self.get_charge_time() + self.get_travel_time()

    def is_charging(self):
        return self._is_charge

    def set_is_charging(self, charge: bool):
        self._is_charge = charge

    def is_decharging(self):
        return self._is_decharge

    def set_is_decharging(self, decharge: bool):
        self._is_decharge = decharge

    def is_bus_stop(self, station: str):
        return station in self._route

    def get_history(self):
        return self._history

    def set_direct(self, direct: bool | str):
        self._direct = direct

    def is_direct(self):
        return self._direct != False

    def get_direct(self):
        return self._direct

    def update_station_direct(self):
        direct = self.get_direct()
        way = direct[0]
        direct = direct[1:]
        self.set_direct(direct)
        return way

    def is_route(self, route: str):
        return route in self._route

    def get_time(self):
        return self._time

    def update_time(self, value: int = 1):
        self._time = self.get_time() + value
