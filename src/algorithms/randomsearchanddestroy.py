import movealgorithm
import random
from .. import board as b
from ..board import Board
from ..enum import *
import logging
from randomsearch import RandomSearch
from destroy import Destroy

State = enum("SEARCHING", "DESTROYING")

class RandomSearchAndDestroy(movealgorithm.MoveAlgorithm):

    def __init__(self):
        self.state = State.SEARCHING
        self.randomSearch = RandomSearch()
        self.lastTarget = None
        self.destroy = None

    def findNextMove(self, board):
        logging.debug("Finding next move...")

        if self.state == State.SEARCHING and self.lastTarget and board.getState(self.lastTarget) == b.State.HIT:
            logging.debug("Last shot was a hit, switching state to DESTROYING")
            self.state = State.DESTROYING
            self.destroy = Destroy(self.lastTarget)

        if self.state == State.SEARCHING:
            self.lastTarget = self.randomSearch.findNextMove(board)
            assert isinstance(self.lastTarget, tuple), "Search move must be a tuple"
            return self.lastTarget
        else:
            result = self.destroy.findNextMove(board)

            if result == movealgorithm.StatusCode.COMPLETED:
                logging.debug("Target destroyed, switching state to SEARCHING")
                self.state = State.SEARCHING
                self.destroy = None
                self.lastTarget = self.randomSearch.findNextMove(board)
                assert isinstance(self.lastTarget, tuple), "Search move must be a tuple"
                return self.lastTarget
            else:
                assert isinstance(result, tuple), "Destroy move must be a tuple"
                return result

        
