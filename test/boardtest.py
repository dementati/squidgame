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


if __name__ == "__main__":
    unittest.main()
