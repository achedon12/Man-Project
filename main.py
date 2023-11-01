import Bus
import time
from Log import Log
from Parser import Parser
from sys import *
from Board import Board

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: main.py <person> <route> <bus>")
        exit(1)

    all_person = Parser.parse_persons(argv[1])
    all_bus = Bus.init()
    all_routes = Parser.parse_routes(argv[2])
    # all_bus = Parser.parse_buses(argv[3])

    board = Board(all_bus, all_person, all_routes)
    Logger = Log("logs", all_person, all_bus)
    starTime = int(time.time())

    while True:
        actual_time = int(time.time()) - starTime
        Logger.next_time(actual_time)
        board.next_time(actual_time, all_routes, Logger)
        time.sleep(1)
