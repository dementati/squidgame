import sys
from enum import enum
from squid import Squid

State = enum('EMPTY', 'MISS', 'HIT')

class Board:
    def __init__(self):
        self.size = (8,8)
        self.board = [[State.EMPTY for x in range(self.size[1])] for x in range(self.size[0])]
        self.squidList = []

    def getState(self, (x, y)):
        assert not self.isOutOfBounds((x, y)), "Position out of bounds"

        return self.board[x][y]

    def getSize(self):
        return self.size

    def getAllSquid(self):
        return self.squidList

    def addSquid(self, squid):
        assert isinstance(squid, Squid), "Invalid parameter type"

        self.squidList.append(squid)

    def fire(self, (x,y)):
        assert not self.isOutOfBounds((x, y)), "Position out of bounds"

        for squid in self.squidList:
            if squid.contains((x,y)):
                self.board[x][y] = State.HIT
                return State.HIT

        self.board[x][y] = State.MISS
        return State.MISS

    def render(self):
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if self.board[x][y] == State.MISS:
                    sys.stdout.write("X")
                elif self.board[x][y] == State.HIT:
                    sys.stdout.write("O")
                else:
                    if any([squid.contains((x,y)) for squid in self.squidList]):
                        sys.stdout.write("%")
                    else:
                        sys.stdout.write(".")
            sys.stdout.write("\n")
        sys.stdout.flush()

    def isOutOfBounds(self, (x,y)):
        return x < 0 or x >= self.size[0] or y < 0 or y >= self.size[1]
