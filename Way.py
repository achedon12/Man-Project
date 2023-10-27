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
    def get_fast_way(departure: str, arrival: str):
        ways = Way.get_way()
        way = ""

        if departure + arrival in ways or arrival + departure in ways:
            way = departure + arrival
        else:
            for key, value in ways.items():
                if departure in key:
                    if arrival in key:
                        way += arrival
                        break
                    else:
                        way += key[1]
                        departure = key[1]
                elif arrival in key:
                    way += arrival
                    if departure in key:
                        way += departure
                        break
                    else:
                        way += key[1]
                        arrival = key[1]

        return way
