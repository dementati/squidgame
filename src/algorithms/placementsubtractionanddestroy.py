import movealgorithm
from .. import board as b
from ..enum import enum
from placementsubtraction import PlacementSubtraction
from destroy import Destroy
import logging

State = enum("SEARCHING", "DESTROYING")

class PlacementSubtractionAndDestroy(movealgorithm.MoveAlgorithm):

    def __init__(self):
        logging.debug("Initiating PlacementSubtractionAndDestroy algorithm")
        self.state = State.SEARCHING
        self.lastMove = None
        self.placementSubtraction = None

    def findNextMove(self, board):
        if self.placementSubtraction == None:
            squidLengths = [len(squid) for squid in board.getLiveSquid()]
            self.placementSubtraction = PlacementSubtraction(board, squidLengths)

        if self.state == State.SEARCHING and self.lastMove and board.getState(self.lastMove) == b.State.HIT:
            logging.debug("Last shot hit, switching state to DESTROYING")
            self.state = State.DESTROYING
        
        if self.state == State.DESTROYING:
            destroy = Destroy(self.lastMove)
            move = destroy.findNextMove(board)
            if move == movealgorithm.StatusCode.COMPLETED:
                logging.debug("Destroy subalgorithm completed, switching state to SEARCHING")
                self.state = State.SEARCHING
            else:
                return move

        if self.state == State.SEARCHING:
            logging.debug("Searching...")
            squidLengths = [len(squid) for squid in board.getLiveSquid()]
            self.placementSubtraction.updateSquidLengths(squidLengths) 
            self.lastMove = self.placementSubtraction.findNextMove(board)
            return self.lastMove
            
