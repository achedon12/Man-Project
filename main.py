import Bus
import Person
import time
from Parser import Parser

from sys import argv

from Board import Board

if __name__ == '__main__':
    all_bus = Bus.init()
    all_person = Parser.parse_persons(argv[1])

    board = Board(all_bus, all_person)
    starTime = int(time.time())

    while True:
        actual_time = int(time.time()) - starTime
        board.next_time(actual_time)
        time.sleep(1)
