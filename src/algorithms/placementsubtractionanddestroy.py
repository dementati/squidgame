import movealgorithm
from .. import board as b
from ..enum import enum
from placementsubtraction import PlacementSubtraction

State = enum("SEARCHING", "DESTROYING")

class PlacementSubtractionAndDestroy(movealgorithm.MoveAlgorithm):

    def __init__(self):
        self.state = State.SEARCHING
        self.lastMove = None

    def findNextMove(self, board):
        if self.state == State.SEARCHING and self.lastMove and board.getState(self.lastMove) == b.State.HIT:
            self.state = State.DESTROYING
        
        if self.state == State.DESTROYING:
            destroy = Destroy(self.lastMove)
            move = destroy.findNextMove(board)
            if move == movealgorithm.StatusCode.COMPLETED:
                self.state == State.SEARCHING
            else:
                return move

        if self.state == State.SEARCHING:
            squidLengths = [len(squid) for squid in board.getLiveSquid()]
            algo = PlacementSubtraction(board, squidLengths)
            self.lastMove = algo.findNextMove(board)
            return self.lastMove
            
