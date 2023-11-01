class Way:

    @staticmethod
    def get_way():
        return {
            'BA': {
                'route_number': 1,
                'time': 10,
            },
            'AC': {
                'route_number': 2,
                'time': 4,
            },
            'CE': {
                'route_number': 4,
                'time': 4,
            },
            'CD': {
                'route_number': 3,
                'time': 12,
            }
        }

    @staticmethod
    def get_fast_way(departure: str, arrival: str, is_return: bool):
        ways = Way.get_way()
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

    @staticmethod
    def get_time_required(departure: str, arrival: str):

        ways = Way.get_way()
        way = departure + arrival
        if way in ways:
            return ways[way]['time']
        elif way[::-1] in ways:
            return ways[way[::-1]]['time']
        else:
            return 0
        pass
