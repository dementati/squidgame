import movealgorithm
from .. import board as b
from ..board import Board
from ..squid import Squid
import logging

class PlacementSubtraction(movealgorithm.MoveAlgorithm):

    def __init__(self, board, squidLengths):
        assert isinstance(board, Board), "Invalid parameter type"
        assert isinstance(squidLengths, list), "Invalid parameter type"

        self.squidLengths = squidLengths
        self.board = board
        self.countPlacementsOnBoard()

    def countPlacementsOnBoard(self):
        logging.debug("Counting placements on board")
        self.placements = []
        for y in range(8):
            for x in range(8):
                pos = (x,y)
                for squidLength in self.squidLengths:
                    self.countPlacementsOnPosition(pos, squidLength)

        self.dirty = False
        return len(self.placements)

    def countPlacementsOnPosition(self, (x, y), squidLength):
        logging.debug("Counting placements on positions %s" % str((x,y)))
        for axis in ["x", "y"]:
            for start in range(-squidLength+1, 1):
                squid = Squid()
                complete = True
                for i in range(squidLength):
                    if axis == "x":
                        pos = (x + start + i, y)
                    else:
                        pos = (x, y + start + i)

                    if self.board.isOutOfBounds(pos) or self.board.getState(pos) != b.State.EMPTY:
                        complete = False
                        break
                    else:
                        squid.getPositions().append(pos)
                
                if complete:
                    if not squid in self.placements:
                        self.placements.append(squid)

    def countRemovablePlacements(self, pos):
        count = 0
        for squid in self.placements:
            if squid.contains(pos):
                count += 1

        return count

    def placementSubtraction(self, board):
        bestMove = None
        bestReduction = 0

        for y in range(8):
            for x in range(8):
                pos = (x,y)
                if board.getState(pos) == b.State.EMPTY:
                    reduction = self.countRemovablePlacements(pos)
                    if reduction > bestReduction:
                        bestMove = pos
                        bestReduction = reduction
        
        return bestMove

    def findNextMove(self, board):
        return self.placementSubtraction(board)
