import unittest
from ..src.board import *

class BoardTest(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_createEmptyBoard(self):
        # THEN
        for y in range(8):
            for x in range(8):
                pos = (x,y)
                self.assertEqual(self.board.getState(pos), State.EMPTY, "Invalid initial state")

    def test_fireOnEmptyBoard(self):
        # GIVEN
        target = (3,3)
        
        # WHEN
        result = self.board.fire(target)

        # THEN
        self.assertEqual(result, State.MISS, "Invalid fire result")
        for y in range(8):
            for x in range(8):
                pos = (x,y)
                if pos == target:
                    self.assertEqual(self.board.getState(pos), State.MISS, "Invalid board state")
                else:
                    self.assertEqual(self.board.getState(pos), State.EMPTY, "Invalid board state")

    def test_fireOnSquid(self):
        # GIVEN
        squid = Squid([(3,3), (3,4)])
        self.board.addSquid(squid)
        target = (3,3)

        # WHEN
        result = self.board.fire(target)

        # THEN
        self.assertEqual(result, State.HIT, "Invalid fire result")
        for y in range(8):
            for x in range(8):
                pos = (x,y)
                if pos == target:
                    self.assertEqual(self.board.getState(pos), State.HIT, "Invalid board state")
                else:
                    self.assertEqual(self.board.getState(pos), State.EMPTY, "Invalid board state")

    def test_renderBoards(self):
        squid = Squid([(0,0), (0,1)])
        self.board.addSquid(squid)
        self.board.fire((3,3))
        self.board.fire((0,1))

        print
        self.board.render()
        print

    def test_isOutOfBounds(self):
        self.assertTrue(self.board.isOutOfBounds((-1,0)), "Position indicated as not out of bounds when it is")
        self.assertTrue(self.board.isOutOfBounds((0,-1)), "Position indicated as not out of bounds when it is")
        self.assertTrue(self.board.isOutOfBounds((-1,-1)), "Position indicated as not out of bounds when it is")
        self.assertTrue(self.board.isOutOfBounds((8,7)), "Position indicated as not out of bounds when it is")
        self.assertTrue(self.board.isOutOfBounds((7,8)), "Position indicated as not out of bounds when it is")
        self.assertTrue(self.board.isOutOfBounds((8,8)), "Position indicated as not out of bounds when it is")
        self.assertFalse(self.board.isOutOfBounds((0,0)), "Position indicated as out of bounds when it isn't")
        self.assertFalse(self.board.isOutOfBounds((7,0)), "Position indicated as out of bounds when it isn't")
        self.assertFalse(self.board.isOutOfBounds((0,7)), "Position indicated as out of bounds when it isn't")
        self.assertFalse(self.board.isOutOfBounds((7,7)), "Position indicated as out of bounds when it isn't")

if __name__ == "__main__":
    unittest.main()
