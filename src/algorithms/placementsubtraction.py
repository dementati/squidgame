import movealgorithm
from .. import board as b
from ..board import Board
from ..squid import Squid
import logging
import copy

class PlacementSubtraction(movealgorithm.MoveAlgorithm):

    placementsTemplate = None

    def __init__(self, board, squidLengths):
        assert isinstance(board, Board), "Invalid parameter type"
        assert isinstance(squidLengths, list), "Invalid parameter type"

        if PlacementSubtraction.placementsTemplate == None:
            PlacementSubtraction.placementsTemplate = PlacementSubtraction.countPlacementsOnBoard(board, squidLengths)

        self.placements = copy.deepcopy(PlacementSubtraction.placementsTemplate)

    @staticmethod
    def countPlacementsOnBoard(board, squidLengths):
        placements = []
        for y in range(8):
            for x in range(8):
                pos = (x,y)
                for squidLength in squidLengths:
                    posPlacements = PlacementSubtraction.countPlacementsOnPosition(board, pos, squidLength)
                    placements += [p for p in posPlacements if not p in placements]
                    
        return placements

    @staticmethod
    def countPlacementsOnPosition(board, (x, y), squidLength):
        placements = []
        for axis in ["x", "y"]:
            for start in range(-squidLength+1, 1):
                squid = Squid([])
                complete = True
                for i in range(squidLength):
                    if axis == "x":
                        pos = (x + start + i, y)
                    else:
                        pos = (x, y + start + i)

                    if board.isOutOfBounds(pos) or board.getState(pos) != b.State.EMPTY:
                        complete = False
                        break
                    else:
                        squid.getPositions().append(pos)
                
                if complete:
                    placements.append(squid)
        return placements

    def countRemovablePlacements(self, pos):
        count = 0
        for squid in self.placements:
            if squid.contains(pos):
                count += 1

        return count

    def removePlacements(self, pos):
        self.placements = [squid for squid in self.placements if not squid.contains(pos)]

    def updateSquidLengths(self, squidLengths):
        self.placements = [squid for squid in self.placements if len(squid) in squidLengths]

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
       
        self.removePlacements(bestMove)
        return bestMove

    def findNextMove(self, board):
        return self.placementSubtraction(board)
