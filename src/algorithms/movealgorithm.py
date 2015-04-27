from ..enum import *

StatusCode = enum("COMPLETED")

class MoveAlgorithm:

    def findNextMove(self, board):
        raise NotImplementedError()
