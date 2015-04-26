import unittest
from boatgame import *

class BoatGameTest(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_shortSquidEmptyBoardCorner(self):
        self.board.countPlacementsOnPosition((0, 0), 2)
        self.assertEqual(len(self.board.placements), 2, "Invalid number of placements")

    def test_shortSquidSingleShotCorner(self):
        self.board.check((0,0))
        self.board.countPlacementsOnPosition((0, 0), 2)
        self.assertEqual(len(self.board.placements), 0, "Invalid number of placements")

    def test_shortSquidSingleShotCorner2(self):
        self.board.check((1,0))
        self.board.countPlacementsOnPosition((0, 0), 2)
        self.assertEqual(len(self.board.placements), 1, "Invalid number of placements")

    def test_longSquidEmptyBoardMiddle(self):
        self.board.countPlacementsOnPosition(self.placements, (4, 4), 4)
        self.assertEqual(len(self.placements), 8, "Invalid number of placements")

    def test_multipleSuccessiveCounts(self):
        self.board.countPlacementsOnPosition(self.placements, (0, 0), 2)
        self.board.countPlacementsOnPosition(self.placements, (0, 1), 2)
        self.assertEquals(len(self.placements), 4, "Invalid number of placements")

if __name__ == "__main__":
    unittest.main()
