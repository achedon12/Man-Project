from Person import Person
from Travel import Travel


class Parser:

    def __init__(self):
        pass

    @staticmethod
    def parse_persons(file: str):
        persons = []

        with open(file) as content:
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
                        travel = Travel(copyLine[index + 1][0], copyLine[index + 1][1], copyLine[index])
                        travels.append(travel)
                    persons.append(Person(f"{name}{i + 1}", travels))
            content.close()

        return persons
