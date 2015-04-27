import movealgorithm
import logging
from .. import board as b
from .. import util

class DestroyParallels(movealgorithm.MoveAlgorithm):
    def __init__(self, parallels):
        assert len(parallels) > 1, "Parallels must indicate at least two side-by-side squid"
        assert util.isStraight(parallels), "Parallels must be on a line"
        assert util.isCoherent(parallels), "Parallels must be coherent"

        self.parallels = parallels

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
                    return self.destroyParallels(board)

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

    def destroyParallels(self, board):
        for pos in self.parallels:
            target = next((pos for squid in board.getAllSquid() if squid.contains(pos) and not board.isSquidDestroyed(squid)), None)
            if target != None:
                break

        if target == None:
            return movealgorithm.StatusCode.COMPLETED

        direction = (self.parallels[0][0] - self.parallels[1][0], self.parallels[0][1] - self.parallels[1][1])
        tmp1 = int(direction[1]/abs(direction[1])) if direction[1] != 0 else 0
        tmp2 = int(direction[0]/abs(direction[0])) if direction[0] != 0 else 0
        direction = (tmp1, tmp2)
        
        return self.finish(board, target, direction)

    def findNextMove(self, board):
        logging.debug("Destroying multiple squid side by side...")
        return self.destroyParallels(board)

