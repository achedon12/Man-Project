from Bus import Bus
from Message import error_board_creation
from Test import test_creation_object
from Travel import Travel


class Board:
    def __init__(self, bus: list, persons: list):
        if test_creation_object([bus, persons]):
            raise Exception(error_board_creation)
        self.bus = bus
        self.persons = persons

    def get_bus(self):
        return self.bus

    def get_persons(self):
        return self.persons

    def decharge(self, bus: Bus, current_station: int, actual_time: int):
        for person in bus.get_passengers():
            current_travel = person.get_current_travel()

            if current_travel is not None and current_travel.get_bus_route_arrive() == current_station:
                bus.set_is_decharging(True)
                person.set_in_bus(False)
                # current_travel.set_etat(2)
                print(f"[DECHARGING] {person.get_name()} exit from the bus {bus.get_bus_number()} at "
                      f"{current_station} ({len(bus.get_passengers()) - 1}/{bus.get_max_passengers()})")
                bus.remove_passenger(person)
                break
            if person.name == bus.get_passengers()[-1].name:
                bus.set_is_decharging(False)

    def charge(self, bus: Bus, current_station: int, actual_time: int):
        for person in self.persons:
            if not person.is_in_bus():
                if not bus.is_full():
                    bus.set_is_charging(True)
                    some_one_enter = False
                    for travel in person.get_travels():
                        if float(travel.get_departure_time()) > float(actual_time):
                            continue

                        if not travel.is_done():
                            if travel.get_bus_route_depart() == current_station and bus.is_bus_stop(
                                    travel.get_bus_route_arrive()):
                                if bus.get_available_seats() > 0:
                                    bus.add_passenger(person)
                                    some_one_enter = True
                                    person.set_in_bus(bus.get_bus_number())
                                    travel.set_etat(Travel.TRAVEL_IN_PROGRESS)
                                    print(
                                        f"[CHARGING] {person.get_name()} enter in the bus {bus.get_bus_number()} at "
                                        f"{bus.get_current_station()} ({len(bus.get_passengers())}/{bus.get_max_passengers()})"
                                        f" for a travel from {travel.get_bus_route_depart()} to {travel.get_bus_route_arrive()}"
                                        f" at {travel.get_departure_time()}")
                                    break
                                else:
                                    print(f"[INFO] bus is full, {person.get_name()} can't enter")
                            if some_one_enter:
                                break
                    if some_one_enter:
                        break
                    if person.name == self.persons[-1].name:
                        bus.set_is_charging(False)
                        break

    def next_station(self, bus: Bus, current_station: int):
        if not bus.is_charging() and not bus.is_decharging():
            bus.move_station()
            print(
                f"[INFO] bus is following the route {bus.get_previous_station_from_history()} to {bus.get_current_station()} from "
                f"his route {bus.get_route()} with {len(bus.get_passengers())} passengers")
        elif bus.is_full():
            print(f"[INFO] bus is full, he can't charge more passengers")
            bus.set_is_charging(False)

    def end_route(self, bus: Bus):
        if not bus.is_charging() or not bus.is_decharging():
            if bus.get_current_station_index() == bus.get_end_route_index() or bus.get_current_station_index() == 0:
                bus.change_etat()
                if bus.get_current_station_index() == bus.get_end_route_index():
                    print("[RETURN] bus is comming back to the start of the route")

    def departure(self, bus: Bus, current_station: int, actual_time: int):
        if current_station == bus.get_start_route():
            print(
                f"[READY] bus is now ready to do the route at time {actual_time}. Departure from {bus.get_start_route()}")

    def stop_decharge(self, bus: Bus):
        if bus.is_empty():
            print("[INFO] bus is empty, he can't decharge more passengers")
            bus.set_is_decharging(False)

    def next_time(self, actual_time: int):
        print(f"\n\n------------------- Temps simulation {actual_time} -------------------")
        for bus in self.bus:
            print(f"\n--------BUS{bus.bus_number}------------")

            current_station = bus.get_current_station()

            # departure
            self.departure(bus, current_station, actual_time)

            # decharge
            self.decharge(bus, current_station, actual_time)

            # charge
            self.charge(bus, current_station, actual_time)

            # next station
            self.next_station(bus, current_station)

            # end of the route
            self.end_route(bus)

            # stop decharge if bus is empty
            self.stop_decharge(bus)
