import unittest
from boatgame import *

class BoatGamePerformanceTest(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_allPlacementsEmptyBoard(self):
        placementCount = self.board.countPlacementsOnBoard()
        print("Placement count: " + str(placementCount))

    def test_getBestMoveOnEmptyBoard(self):
        bestMove, bestReduction = self.board.findBestMove()
        print("Best move is (%d, %d) with a %d placement reduction." % (bestMove[0], bestMove[1], bestReduction)) 

if __name__ == "__main__":
    unittest.main()
