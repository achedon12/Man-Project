from os import path, mkdir, listdir, remove


class Log:
    def __init__(self, log_repository: str, persons: list, buses: list):
        self._log_repository = log_repository
        self._persons = persons
        self._buses = buses

        if not path.exists(self._log_repository):
            mkdir(self._log_repository)

        if not path.exists(self.get_log_repository_type("persons")):
            mkdir(self.get_log_repository_type("persons"))
        else:
            for file in listdir(self.get_log_repository_type("persons")):
                if file.endswith(".txt"):
                    remove(self.get_log_repository_type("persons") + "/" + file)

        if not path.exists(self.get_log_repository_type("bus")):
            mkdir(self.get_log_repository_type("bus"))
        else:
            for file in listdir(self.get_log_repository_type("bus")):
                if file.endswith(".txt"):
                    remove(self.get_log_repository_type("bus") + "/" + file)

    def next_time(self, time: int):
        for person in self._persons:
            self.log(person.name, person.__str__(), "persons", time)

        for bus in self._buses:
            self.log("Bus" + str(bus.bus_number), bus.__str__(), "bus", time)

    def log(self, file: str, message: str, type: str, time: int, end: str = "\n"):
        with open(self.get_file(type, file), 'a') as f:
            f.write(f"---------------------- Time: {time} ----------------------\n")
            f.write(message + end)

    def get_log_repository(self):
        return self._log_repository

    def get_log_repository_type(self, type: str):
        return self._log_repository + "/" + type

    def get_file(self, type: str, file: str):
        return self.get_log_repository_type(type) + "/" + file + ".txt"
