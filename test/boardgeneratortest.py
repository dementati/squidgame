import unittest
from ..src.boardgenerator import *
from ..src.board import *

class BoardGeneratorTest(unittest.TestCase):

    def test_generateBoard(self):
        bg = BoardGenerator()
        board = bg.generate()
        board.render()

if __name__ == "__main__":
    unittest.main()
