from Message import *
from Person import Person
from Test import test_creation_object


def init(way: dict):
    bus1 = Bus(1, 10, 1, 30, 'BACECA')
    bus2 = Bus(2, 10, 1, 30, 'DCEC')
    bus3 = Bus(3, 10, 1, 30, 'BED')
    bus4 = Bus(4, 2, 1, 10, 'AC')
    return [bus1, bus2, bus3, bus4]


class Bus:

    def __init__(self, bus_number: int, max_passengers: int, charge_speed: int, travel_speed: int, route: str):
        if test_creation_object([bus_number, max_passengers, charge_speed, travel_speed, route]):
            raise Exception(error_bus_creation(bus_number))
        self._bus_number = bus_number
        self._charge_speed = charge_speed
        self._travel_speed = travel_speed
        self._route = route
        self._passengers = []
        self._current_station = self._route[0]
        self._max_passengers = max_passengers
        self._is_charge = False
        self._is_decharge = False
        self._history = ""
        self._direct = False

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

    def add_passenger(self, passenger):
        self._passengers.append(passenger)

    def remove_passenger(self, passenger: Person):
        self._passengers.remove(passenger)

    def move_station(self):
        self._history += self._current_station
        if self.is_direct():
            self._current_station = self.update_station_direct()
        else:
            self._current_station = self.get_next_station()

    def get_next_station(self):
        index = self._route.index(self._current_station)
        if index == self.get_end_route_index():
            return self._route[index - 1]
        if self._etat:
            return self._route[index - 1]
        return self._route[index + 1]

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
        print(self._route, self._current_station)
        # TODO: fix this to continue
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
        if type(direct) == str:
            way = direct[0]
            print(direct)
            self.set_direct(direct[1:])
            print(direct)
            return way
