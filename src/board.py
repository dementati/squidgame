import sys
from enum import enum
from squid import Squid
import logging

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

    def getLiveSquid(self):
        return [squid for squid in self.squidList if not self.isSquidDestroyed(squid)]

    def addSquid(self, squid):
        assert isinstance(squid, Squid), "Invalid parameter type"

        self.squidList.append(squid)

    def fire(self, (x,y)):
        assert not self.isOutOfBounds((x, y)), "Position out of bounds"

        logging.debug("Firing on %s", str((x,y)))

        for squid in self.squidList:
            if squid.contains((x,y)):
                logging.debug("Hit squid")
                self.board[x][y] = State.HIT
                return State.HIT

        logging.debug("It was a miss")
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

    def isWon(self):
        return all([all([self.getState(pos) == State.HIT for pos in squid.getPositions()]) for squid in self.squidList])

    def isSquidDestroyed(self, squid):
        assert squid in self.squidList, "Supplied squid is not on the board"

        return all([self.getState(pos) == State.HIT for pos in squid.getPositions()])
