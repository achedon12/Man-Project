import Bus
import time
from Log import Log
from Parser import Parser

from sys import *

from Board import Board

if __name__ == '__main__':
    all_bus = Bus.init()
    all_person = Parser.parse_persons(argv[1])

    board = Board(all_bus, all_person)
    Logger = Log("logs", all_person, all_bus)
    starTime = int(time.time())

    while True:
        actual_time = int(time.time()) - starTime
        board.next_time(actual_time)
        Logger.next_time(actual_time)
        time.sleep(1)
