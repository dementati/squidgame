import movealgorithm
import random
from ..board import *

class RandomSearch(movealgorithm.MoveAlgorithm):

    def findNextMove(self, board):
        size = board.getSize()
        emptyPositions = []
        for y in range(size[1]):
            for x in range(size[0]):
                if board.getState((x,y)) == State.EMPTY:
                    emptyPositions.append((x,y))

        return random.choice(emptyPositions)
