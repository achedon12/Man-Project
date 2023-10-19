from Message import *
from Person import Person
from Test import test_creation_object


def init():
    bus1 = Bus(1, 10, 1, 30, 'BACECA')
    bus2 = Bus(2, 10, 1, 30, 'DCEC')
    bus3 = Bus(3, 10, 1, 30, 'BED')
    bus4 = Bus(4, 2, 1, 10, 'AC')
    return [bus1, bus2, bus3, bus4]


class Bus:

    def __init__(self, bus_number: int, max_passengers: int, charge_speed: int, travel_speed: int, route: str):
        if test_creation_object([bus_number, max_passengers, charge_speed, travel_speed, route]):
            raise Exception(error_bus_creation(bus_number))
        self.bus_number = bus_number
        self.charge_speed = charge_speed
        self.travel_speed = travel_speed
        self.route = route
        self.passengers = []
        self.current_station = self.route[0]
        self.max_passengers = max_passengers
        self.is_charge = False
        self.is_decharge = False
        self.history = ""

        # True = going to the end of the route
        self.etat = False

    def __str__(self):
        return f"Bus {self.bus_number} is at station {self.current_station} with {len(self.passengers)} passengers"

    def get_passengers(self):
        return self.passengers

    def get_current_station(self):
        return self.current_station

    def get_bus_number(self):
        return self.bus_number

    def get_charge_speed(self):
        return self.charge_speed

    def get_travel_speed(self):
        return self.travel_speed

    def get_route(self):
        return self.route

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def remove_passenger(self, passenger: Person):
        self.passengers.remove(passenger)

    def move_station(self):
        self.history += self.current_station
        self.current_station = self.get_next_station()

    def get_next_station(self):
        index = self.route.index(self.current_station)
        if index == self.get_end_route_index():
            return self.route[index - 1]
        if self.etat:
            return self.route[index - 1]
        return self.route[index + 1]

    def get_previous_station(self):
        index = self.route.index(self.current_station)
        if self.etat:
            return self.route[index + 1]
        return self.route[index - 1]

    def get_previous_station_from_history(self):
        if self.history == "":
            return self.current_station
        return self.history[-1]

    def get_max_passengers(self):
        return self.max_passengers

    def get_etat(self):
        return self.etat

    def change_etat(self):
        self.etat = not self.etat
        return self.etat

    def can_charge(self):
        return self.etat

    def get_end_route(self):
        return self.route[-1]

    def get_start_route(self):
        return self.route[0]

    def get_end_route_index(self):
        return len(self.route) - 1

    def get_current_station_index(self):
        return self.route.index(self.current_station)

    def is_full(self):
        return len(self.passengers) >= self.max_passengers

    def get_available_seats(self):
        return self.max_passengers - len(self.passengers)

    def get_charge_time(self):
        return self.max_passengers * self.charge_speed

    def get_travel_time(self):
        return len(self.route) * self.travel_speed

    def get_total_time(self):
        return self.get_charge_time() + self.get_travel_time()

    def is_charging(self):
        return self.is_charge

    def set_is_charging(self, charge: bool):
        self.is_charge = charge

    def is_decharging(self):
        return self.is_decharge

    def set_is_decharging(self, decharge: bool):
        self.is_decharge = decharge

    def is_bus_stop(self, station: str):
        return station in self.route

    def get_history(self):
        return self.history
