import unittest
from ...src.board import Board
from ...src.algorithms.placementsubtraction import PlacementSubtraction

class PlacementSubtractionTest(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()

    def test_shortSquidEmptyBoardCorner(self):
        placements = PlacementSubtraction.countPlacementsOnPosition(self.board, (0, 0), 2)
        self.assertEqual(len(placements), 2, "Invalid number of placements")

    def test_shortSquidSingleShotCorner(self):
        self.board.fire((0,0))
        placements = PlacementSubtraction.countPlacementsOnPosition(self.board, (0, 0), 2)
        self.assertEqual(len(placements), 0, "Invalid number of placements")

    def test_shortSquidSingleShotCorner2(self):
        self.board.fire((1,0))
        placements = PlacementSubtraction.countPlacementsOnPosition(self.board, (0, 0), 2)
        self.assertEqual(len(placements), 1, "Invalid number of placements")

    def test_longSquidEmptyBoardMiddle(self):
        placements = PlacementSubtraction.countPlacementsOnPosition(self.board, (4, 4), 4)
        self.assertEqual(len(placements), 8, "Invalid number of placements")

    def test_countPlacementsOnBoard(self):
        placements = PlacementSubtraction.countPlacementsOnBoard(self.board, [2, 3, 4])
        self.assertEquals(len(placements), 288, "Invalid number of placements")

    def test_countRemovablePlacements(self):
        placementSubtraction = PlacementSubtraction(self.board, [2,3,4])

        # TODO: Add more tests

        self.assertEquals(placementSubtraction.countRemovablePlacements((3,3)), 18, "Invalid number of removable placements")
        self.assertEquals(placementSubtraction.countRemovablePlacements((2,3)), 17, "Invalid number of removable placements")
        self.assertEquals(placementSubtraction.countRemovablePlacements((1,3)), 15, "Invalid number of removable placements")
        self.assertEquals(placementSubtraction.countRemovablePlacements((0,3)), 12, "Invalid number of removable placements")
        self.assertEquals(placementSubtraction.countRemovablePlacements((2,2)), 16, "Invalid number of removable placements")
        self.assertEquals(placementSubtraction.countRemovablePlacements((1,1)), 12, "Invalid number of removable placements")
        self.assertEquals(placementSubtraction.countRemovablePlacements((0,0)), 6, "Invalid number of removable placements")

    # TODO: Add more tests

if __name__ == "__main__":
    unittest.main()
