import Bus
import time
from Log import Log
from Parser import Parser

from sys import *

from Board import Board
from Way import Way

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: main.py <file>")
        exit(1)

    all_person = Parser.parse_persons(argv[1])
    all_way = Way.get_way()
    all_bus = Bus.init()

    board = Board(all_bus, all_person)
    Logger = Log("logs", all_person, all_bus)
    starTime = int(time.time())

    while True:
        actual_time = int(time.time()) - starTime
        Logger.next_time(actual_time)
        board.next_time(actual_time, all_way, Logger)
        time.sleep(1)
