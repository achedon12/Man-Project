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

    def next_time(self, actual_time: int):
        for bus in self.bus:
            print(f"\n--------BUS{bus.bus_number}------------")

            current_station = bus.get_current_station()

            # departure
            if current_station == bus.get_start_route():
                print(f"[READY] bus is now ready to do the route. Departure from {bus.get_start_route()}")

            #  decharge
            # some_one_exit = False
            # if bus.get_previous_station() != bus.get_current_station():
            #     for person in self.persons:
            #         if person.is_in_bus_number(bus.bus_number):
            #             current_travel = person.get_current_travel()
            #             if current_travel.get_bus_route_arrive() == current_station:
            #                 if not some_one_exit:
            #                     some_one_exit = True
            #                     bus.remove_passenger(person)
            #                     person.set_in_bus(False)
            #                     current_travel.set_etat(Travel.TRAVEL_DONE)
            #                     print(f"[DECHARGING] {person.get_name()} exit from the bus {bus.get_bus_number()} at "
            #                           f"{bus.get_current_station()} ({len(bus.get_passengers())}/{bus.get_max_passengers()})")
            #                     break

            # decharge


            # charge
            for person in self.persons:
                if not person.is_in_bus():
                    if not bus.is_full():
                        bus.set_is_charging(True)
                        some_one_enter = False

                        for travel in person.get_travels():
                            if travel.get_bus_route_depart() == current_station and bus.is_bus_stop(
                                    travel.get_bus_route_arrive()):
                                if bus.get_available_seats() > 0:
                                    bus.add_passenger(person)
                                    some_one_enter = True
                                    person.set_in_bus(bus.get_bus_number())
                                    travel.set_etat(Travel.TRAVEL_IN_PROGRESS)
                                    print(f"[CHARGING] {person.get_name()} enter in the bus {bus.get_bus_number()} at "
                                          f"{bus.get_current_station()} ({len(bus.get_passengers())}/{bus.get_max_passengers()})")
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

            # next station
            if not bus.is_charging():
                bus.move_station()
                print(
                    f"[INFO] bus is following the route {bus.get_previous_station()} to {bus.get_current_station()} from "
                    f"his route {bus.get_route()} with {len(bus.get_passengers())} passengers")
            elif bus.is_full():
                print(f"[INFO] bus is full, he can't charge more passengers")
                bus.set_is_charging(False)

            # end of the route
            if bus.get_current_station_index() == bus.get_end_route_index() or bus.get_current_station_index() == 0:
                bus.change_etat()
                if bus.get_current_station_index() == bus.get_end_route_index():
                    print("[RETURN] bus is comming back to the start of the route")
