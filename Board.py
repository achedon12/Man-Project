from Message import error_board_creation
from Test import test_creation_object
from Travel import Travel
from Log import *


class Board:
    def __init__(self, bus: list, persons: list, ways: dict):
        if test_creation_object([bus, persons]):
            raise Exception(error_board_creation)
        self._bus = bus
        self._ways = ways
        self._persons = persons
        self._logger = None

    def get_bus(self):
        return self._bus

    def get_persons(self):
        return self._persons

    def decharge(self, bus: Bus, current_station: int, actual_time: int):
        if bus.is_route(bus.get_current_station()):
            if bus.is_empty():
                bus.set_is_decharging(False)
            else:
                for person in bus.get_passengers():
                    current_travel = person.get_current_travel()
                    if current_travel is not None and current_travel.get_bus_route_arrive() == current_station:
                        bus.set_is_decharging(True)
                        person.set_in_bus(False)
                        current_travel.set_etat(Travel.TRAVEL_DONE)

                        self.log(bus,
                                 f"[DECHARGING] {person.get_name()} exit from the bus {bus.get_bus_number()} at {current_station} ({len(bus.get_passengers()) - 1}/{bus.get_max_passengers()})")
                        self.log(person,
                                 f"[DECHARGING] {person.get_name()} exit from the bus {bus.get_bus_number()} at {current_station} ({len(bus.get_passengers()) - 1}/{bus.get_max_passengers()})")

                        bus.remove_passenger(person)
                        break
                    if person.get_name() == bus.get_passengers()[-1].get_name():
                        bus.set_is_decharging(False)
        else:
            self.log(bus, f"[INFO] bus is direct, he can't decharge passengers at station {bus.get_current_station()}")

    def charge(self, bus: Bus, current_station: int, actual_time: int):
        if bus.is_route(bus.get_current_station()):
            for person in self._persons:
                if not person.is_in_bus():
                    if not bus.is_full():
                        bus.set_is_charging(True)
                        some_one_enter = False
                        for index in range(len(person.get_travels())):
                            travel = person.get_travel(index)
                            if float(travel.get_departure_time()) > float(actual_time):
                                continue

                            if not travel.is_done() and travel.is_not_started():
                                if travel.get_bus_route_depart() == current_station and bus.is_bus_stop(
                                        travel.get_bus_route_arrive()):
                                    if bus.get_available_seats() > 0:
                                        bus.add_passenger(person)
                                        some_one_enter = True
                                        person.set_in_bus(bus.get_bus_number())
                                        travel.set_etat(Travel.TRAVEL_IN_PROGRESS)
                                        self.log(bus,
                                                 f"[CHARGING] {person.get_name()} enter in the bus {bus.get_bus_number()} at "
                                                 f"{bus.get_current_station()} ({len(bus.get_passengers())}/{bus.get_max_passengers()})"
                                                 f" for a travel from {travel.get_bus_route_depart()} to {travel.get_bus_route_arrive()}"
                                                 f" at {travel.get_departure_time()}")
                                        self.log(person, f"[INFO] enter in the bus {bus.get_bus_number()} at "
                                                         f"{bus.get_current_station()} ({len(bus.get_passengers())}/{bus.get_max_passengers()})"
                                                         f" for a travel from {travel.get_bus_route_depart()} to {travel.get_bus_route_arrive()}"
                                                         f" at {travel.get_departure_time()}")
                                        break
                                    else:
                                        self.log(bus, f"[INFO] bus is full, {person.get_name()} can't enter")
                                if some_one_enter:
                                    break
                        if some_one_enter:
                            break
                        if person.get_name() == self._persons[-1].get_name():
                            bus.set_is_charging(False)
                            break
        else:
            self.log(bus, f"[INFO] bus is direct, he can't charge passengers at station {bus.get_current_station()}")

    def get_percent(self, current_time: int, time_required: int):
        return round((current_time / time_required) * 100)

    def next_station(self, bus: Bus, current_station: int, ways: list):
        self.move_bus(bus, ways)

    def travel(self, bus: Bus):
        next_station = bus.get_next_station()
        current_station = bus.get_current_station()
        current_time = bus.get_time()
        time_required = self.get_time_required(current_station, next_station)

        return current_time >= time_required

    def set_direct(self, bus: Bus, ways: list, departure: str = None, arrival: str = None):
        if not bus.is_direct():
            if departure is None:
                for index in range(len(bus.get_route())):
                    if index > len(bus.get_route()) - 2:
                        break
                    current_station = bus.get_route()[index]
                    next_station = bus.get_route()[index + 1]
                    way = current_station + next_station
                    if way not in ways and way[::-1] not in ways:
                        bus.set_direct(self.get_fast_way(current_station, next_station, bus.get_etat()))
                        self.log(bus,
                                 f"[INFO] bus {bus.get_bus_number()} is now direct from {current_station} to {next_station}"
                                 f" with his new route {bus.get_direct()}")
                        break
            else:
                bus.set_direct(self.get_fast_way(departure, arrival, bus.get_etat()))
                if bus.get_etat():
                    self.log(bus, f"[INFO] bus {bus.get_bus_number()} is now direct from {arrival} to {departure}"
                                  f" with his new route {bus.get_direct()}")
                else:
                    self.log(bus, f"[INFO] bus {bus.get_bus_number()} is now direct from {departure} to {arrival}"
                                  f" with his new route {bus.get_direct()}")

    def set_no_longer_direct(self, bus: Bus, ways: list):
        if bus.is_direct():
            if len(bus.get_direct()) == 0:
                bus.set_direct(False)
                self.log(bus, f"[INFO] bus is no longer direct")

                # end route
                self.end_route(bus)

                current_station = bus.get_current_station()
                next_station = bus.get_next_station()
                if current_station + next_station not in ways or next_station + current_station not in ways:
                    if bus.get_etat():
                        self.set_direct(bus, ways, next_station, current_station)
                    else:
                        self.set_direct(bus, ways, current_station, next_station)

    def move_bus(self, bus: Bus, ways: list):
        if not bus.is_charging() and not bus.is_decharging():
            if self.travel(bus):
                bus.move_station()
                self.log(bus,
                         f"[INFO] bus is following the route {bus.get_previous_station_from_history()} to {bus.get_current_station()} from "
                         f"his route {bus.get_route()} with {len(bus.get_passengers())} passengers")
                self.set_no_longer_direct(bus, ways)
            else:
                bus.update_time()
                next_station = bus.get_next_station()
                current_station = bus.get_current_station()
                current_time = bus.get_time()
                time_required = self.get_time_required(current_station, next_station)
                self.log(bus,
                         f"[INFO] bus is traveling from {current_station} to {next_station} ({self.get_percent(current_time, time_required)}%)")

        elif bus.is_full():
            self.log(bus, f"[INFO] bus is full, he can't charge more passengers")
            bus.set_is_charging(False)

    def end_route(self, bus: Bus):
        if not bus.is_charging() or not bus.is_decharging():
            current_station_index = bus.get_current_station_index()
            if current_station_index == bus.get_end_route_index() or current_station_index == 0:
                bus.change_etat()
                if bus.get_current_station_index() == bus.get_end_route_index():
                    self.log(bus, "[RETURN] bus is comming back to the start of the route")

    def departure(self, bus: Bus, current_station: int, actual_time: int):
        if current_station == bus.get_start_route():
            self.log(bus,
                     f"[READY] bus is now ready to do the route at time {actual_time}. Departure from {bus.get_start_route()}")

    def stop_decharge(self, bus: Bus):
        if bus.is_empty() and not bus.is_direct():
            message = "[INFO] bus is empty, he can't decharge more passengers"
            self.log(bus, message)
            bus.set_is_decharging(False)

    def simulation_time(self, actual_time: int):
        print(f"\n\n------------------- Temps simulation {actual_time} -------------------")

    def next_time(self, actual_time: int, ways: list, logger: Log):

        # init logger
        if self._logger is None:
            self._logger = logger

        self.simulation_time(actual_time)

        for bus in self._bus:
            print(f"\n--------BUS{bus.get_bus_number()}------------")

            current_station = bus.get_current_station()

            # departure
            self.departure(bus, current_station, actual_time)

            # direct
            self.set_direct(bus, ways)

            # decharge
            self.decharge(bus, current_station, actual_time)

            # charge
            self.charge(bus, current_station, actual_time)

            # next station
            self.next_station(bus, current_station, ways)

            # stop decharge if bus is empty
            self.stop_decharge(bus)

    def log(self, data: object, message: str):
        logger = self.get_logger()
        if isinstance(data, Bus):
            logger.log("Bus" + str(data.get_bus_number()), message, "bus")
        elif isinstance(data, Person):
            logger.log(data.get_name(), message, "persons")
        print(message)

    def get_logger(self):
        return self._logger

    def get_routes(self):
        return self._ways

    def get_fast_way(self, departure: str, arrival: str, is_return: bool):
        ways = self.get_ways()
        way = ""
        initial_departure = departure

        if departure + arrival in ways:
            way = departure + arrival
        elif arrival + departure in ways:
            way = arrival + departure
        else:
            for key, value in ways.items():

                # return way if the bus is in the opposite direction
                if key[1] == departure:
                    key = key[1] + key[0]

                if departure in key:
                    if arrival in key:
                        way += arrival
                        break
                    else:
                        way += key[1]
                        departure = key[1]
                elif arrival in key:
                    if departure in key:
                        way += departure
                        break
                    else:
                        way += key[1]
                        arrival = key[1]

        if is_return:
            way = way[::-1]
            way = way[1:]
            way += initial_departure
        return way

    def get_time_required(self, departure: str, arrival: str):

        ways = self.get_ways()
        way = departure + arrival
        if way in ways:
            return ways[way]['time']
        elif way[::-1] in ways:
            return ways[way[::-1]]['time']
        else:
            return 0
        pass

    def get_ways(self):
        return self._ways
