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
                line = line.replace("\n", "")
                line = line.split(" ")
                number = line[0]
                name = line[1]
                line = line[2:]
                travels = []
                while len(line) > 0:
                    index = 0
                    travels.append(Travel(line[index + 1][0], line[index + 1][1], line[index]))
                    line = line[2:]

                for i in range(int(number)):
                    persons.append(Person(f"{name}{i + 1}", travels))
            content.close()

        return persons
