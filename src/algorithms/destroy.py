import movealgorithm
from .. import board as b
from ..board import Board
from ..enum import *
import logging
from destroyparallels import DestroyParallels

class Destroy(movealgorithm.MoveAlgorithm):
    def __init__(self, lastTarget):
        self.lastTarget = lastTarget
        self.destroyParallels = None

    def finish(self, board, target, direction):
        reverse = False
        hits = [target]
        while True:
            newTarget = (target[0] + direction[0], target[1] + direction[1])
            logging.debug("Checking new target %s" % str(newTarget))

            if board.isOutOfBounds(newTarget) or board.getState(newTarget) == b.State.MISS:
                if reverse:
                    logging.debug("Reversing for the second time, this means multiple squid are side by side, initiating DestroyParallels subalgorithm")
                    hits = list(set(hits))
                    self.destroyParallels = DestroyParallels(hits)
                    return self.destroyParallels.findNextMove(board)

                logging.debug("Target is a miss, inverting search direction")
                direction = (-direction[0], -direction[1])
                reverse = True
                continue

            if board.getState(newTarget) == b.State.EMPTY:
                logging.debug("Target is empty, fire at will")
                return newTarget
    
            logging.debug("Target is a previous hit, continuing in the same direction")
            hits.append(newTarget)
            target = newTarget


    def destroy(self, board):
        logging.debug("Destroying...")
        logging.debug("Last target was %s" % str(self.lastTarget))

        t = self.lastTarget
        assert board.getState(t) == b.State.HIT, "Last target (%d,%d) was %s, expected 2" % (t[0], t[1], str(board.getState(t)))

        hitSquid = next((squid for squid in board.getAllSquid() if squid.contains(t)), None)
        assert hitSquid != None, "No squid at last targeted position"

        if board.isSquidDestroyed(hitSquid):
            logging.debug("Targeted squid destroyed")
            return movealgorithm.StatusCode.COMPLETED 

        neighbours = [(t[0] - 1, t[1]) , (t[0] + 1, t[1]), (t[0], t[1] - 1), (t[0], t[1] + 1)]
        neighbours = filter(lambda n: not board.isOutOfBounds(n), neighbours)

        if any([board.getState(n) == b.State.HIT for n in neighbours]):
            logging.debug("Found multiple hits in a row, attempting to finish off target")
            secondHit = next(n for n in neighbours if board.getState(n) == b.State.HIT)
            direction = (secondHit[0] - t[0], secondHit[1] - t[1])
            
            return self.finish(board, secondHit, direction)

        neighbours = filter(lambda n: board.getState(n) == b.State.EMPTY, neighbours)
        logging.debug("Attempting to fire on an empty neighbour")
        return neighbours[0]

    def findNextMove(self, board):
        if self.destroyParallels:
            return self.destroyParallels.findNextMove(board)
        else:
            return self.destroy(board)
