import random
from board import *

class BoardGenerator:

    def getStartingPosition(self, board):
        size = board.getSize()
        emptyPositions = []
        for y in range(size[1]):
            for x in range(size[0]):
                pos = (x,y)
                if board.getState(pos) == State.EMPTY:
                    emptyPositions.append(pos)

        assert len(emptyPositions) > 0, "Cannot get a starting position on a full board"

        return random.choice(emptyPositions)

    def getDirection(self, board, startPos, squidLength):
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        while directions:
            direction = random.choice(directions)
            directions.remove(direction)

            clear = True
            for i in range(1, squidLength):
                pos = (startPos[0] + i * direction[0], startPos[1] + i * direction[1])
                if board.isOutOfBounds(pos) or board.getState(pos) != State.EMPTY:
                    clear = False
                    break

            if clear:
                return direction

        return None

    def generate(self):
        board = Board()

        for squidLength in [2, 3, 4]:
            direction = None
            while direction == None:
                startPos = self.getStartingPosition(board)
                direction = self.getDirection(board, startPos, squidLength)

                positions = []
                for i in range(squidLength):
                    positions.append((startPos[0] + i * direction[0], startPos[1] + i * direction[1]))
                squid = Squid(positions)

                if any([otherSquid.overlapsWith(squid) for otherSquid in board.getAllSquid()]):
                    direction = None
                else:
                    board.addSquid(squid)

        return board 

