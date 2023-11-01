from Bus import Bus
from Person import Person
from Way import Way
from Travel import Travel


class Parser:

    @staticmethod
    def parse_persons(file: str):
        persons = []

        with open(file, 'r', encoding='utf-8') as content:
            lines = content.readlines()
            for line in lines:
                settings = line.split(" ")
                settings[len(settings) - 1] = settings[len(settings) - 1].replace("\n", "")
                number = settings[0]
                name = settings[1]
                for i in range(int(number)):
                    copyLine = settings[2:]
                    travels = []
                    for index in range(len(copyLine)):
                        if index % 2 != 0:
                            continue
                        travel = Travel(copyLine[index + 1][0], copyLine[index + 1][1], int(copyLine[index]))
                        travels.append(travel)
                    persons.append(Person(f"{name}{i + 1}", travels))
            content.close()

        return persons

    @staticmethod
    def parse_routes(file: str):
        routes = []
        number = 1
        with open(file, 'r', encoding='utf-8') as content:
            lines = content.readlines()
            for line in lines:
                settings = line.split(" ")
                settings[len(settings) - 1] = settings[len(settings) - 1].replace("\n", "")
                departure = settings[1]
                arrival = settings[2]
                time = settings[3]

                time_setting = time[-1]
                time = time[:-1]

                if time_setting.lower() == "m":
                    time = int(time) * 60
                elif time_setting.lower() == "h":
                    time = int(time) * 3600
                else:
                    time = int(time)

                routes.append(Way(number, departure, arrival, time))
                number += 1
            content.close()

        return Parser.convert_list_into_dict(routes, "routes")

    @staticmethod
    def parse_buses(file: str):
        buses = []
        with open(file, 'r', encoding='utf-8') as content:
            lines = content.readlines()
            for index in range(len(lines)):
                line = lines[index]
                settings = line.split(" ")
                settings[len(settings) - 1] = settings[len(settings) - 1].replace("\n", "")
                if settings[0].isdigit():
                    settings_bus = line.replace("\n", "").split(" ")
                    bus_numbers = settings_bus[0]
                    bus_type = settings_bus[2].lower()
                    settings_capacity = lines[index + 1].replace("\n", "").split(" ")
                    capacity = settings_capacity[1]
                    settings_charge_speed = lines[index + 2].replace("\n", "").split(" ")
                    charge = settings_charge_speed[1]
                    settings_travel_speed = lines[index + 3].replace("\n", "").split(" ")
                    distance = settings_travel_speed[1][:-1]
                    time = settings_travel_speed[2]
                    index = index + 3
                    for i in range(int(bus_numbers)):
                        buses.append(Bus(i + 1, int(capacity), int(charge), int(distance) / int(time), bus_type))

        return buses

    @staticmethod
    def convert_list_into_dict(content: list, type: str):
        elements = {}
        if type == "routes":

            for item in content:
                elements[item.get_route()] = {
                    "route_number": item.get_route_number(),
                    "time": item.get_time()
                }

        return elements
