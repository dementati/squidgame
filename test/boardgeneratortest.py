import unittest
from ..src.boardgenerator import *
from ..src.board import *

class BoardGeneratorTest(unittest.TestCase):

    def test_generateBoard(self):
        for i in range(1000):
            bg = BoardGenerator()
            board = bg.generate()

            self.assertFalse(any([any([board.isOutOfBounds(pos) for pos in squid.getPositions()]) for squid in board.getAllSquid()]), "Some squid are out of bounds")
                    
            self.assertFalse(any([any([squid.overlapsWith(otherSquid) for squid in board.getAllSquid() if squid != otherSquid]) for otherSquid in board.getAllSquid()]), "Generated board contains overlapping squid")

    def test_renderGeneratedBoard(self):
        bg = BoardGenerator()
        board = bg.generate()
        print()
        board.render()
        print()

if __name__ == "__main__":
    unittest.main()
