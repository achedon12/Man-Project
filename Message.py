def error_bus_creation(bus: int):
    return "Error: Bus cannot be created: " + str(bus)


def error_person_creation(name: str):
    return "Error: Person cannot be created: " + name


def error_travel_creation(bus_route_depart: str, bus_route_arrive: str, departure_time: int):
    return "Error: Travel cannot be created: " + bus_route_depart + " to " + bus_route_arrive + " at " + str(
        departure_time)


def error_travel_add_person(name: str):
    return f"Error: impossible to add a travel to {name} because it is not defined"


def error_board_creation():
    return "Error: Board cannot be created: "


def error_route_creation(departure: str, arrival: str, time: int):
    return "Error: Route cannot be created: " + departure + " to " + arrival + " in " + str(time)
