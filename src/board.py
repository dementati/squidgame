from enum import enum
from squid import Squid

State = enum('EMPTY', 'MISS', 'HIT')

class Board:
    def __init__(self):
        self.board = [[State.EMPTY for x in range(8)] for x in range(8)]
        self.squidList = []

    def getState(self, (x, y)):
        assert x >= 0 and x <= 7, "Position out of bounds"
        assert y >= 0 and y <= 7, "Position out of bounds"

        return self.board[x][y]

    def addSquid(self, squid):
        assert isinstance(squid, Squid), "Invalid parameter type"

        self.squidList.append(squid)

    def fire(self, (x,y)):
        assert x >= 0 and x <= 7, "Position out of bounds"
        assert y >= 0 and y <= 7, "Position out of bounds"

        for squid in self.squidList:
            if squid.contains((x,y)):
                self.board[x][y] = State.HIT
                return State.HIT

        self.board[x][y] = State.MISS
        return State.MISS
