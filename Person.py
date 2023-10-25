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
        str = f"{self.name} has {len(self.travels)} travels\n"
        for travel in self.travels:
            str += f"\t{travel}\n"
        return str

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

    def get_done_travels(self):
        done_travels = []
        for travel in self.travels:
            if travel.is_done() or travel.is_in_travel():
                done_travels.append(travel)
        return done_travels

    def remove_travel(self, travel: Travel):
        self.travels.remove(travel)

    @staticmethod
    def get_person_from_name(person_name: str, persons: list):
        for person in persons:
            if person.name == person_name:
                return person
        return None
