from Message import *
from Travel import Travel
from Test import test_creation_object


class Person:

    def __init__(self, name: str, travels: list):
        if test_creation_object([name, {
            "type": Travel,
            "values": travels
        }]):
            raise Exception(error_person_creation(name))
        self.name = name
        self.travels = travels
        self.in_bus = False

    def get_travels(self):
        return self.travels

    def get_name(self):
        return self.name

    def __str__(self):
        return f"{self.name} has {len(self.travels)} travels"

    def get_travels(self):
        return self.travels

    def get_travel(self, index):
        return self.travels[index]

    def get_travel_departure(self, index):
        return self.travels[index].get_departure()

    def is_in_bus(self):
        return self.in_bus != False

    def is_in_bus_number(self, bus_number: int):
        return self.in_bus == bus_number

    def set_in_bus(self, etat: int):
        self.in_bus = etat

    def get_current_travel(self):
        for travel in self.travels:
            if travel.is_in_travel():
                return travel
