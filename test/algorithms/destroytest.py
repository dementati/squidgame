import unittest
from ...src.algorithms.destroy import *
from ...src import board
from ...src.squid import Squid
import logging

class DestroyTest(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)

    def test_singleShortSquidHit(self):
        # GIVEN
        board1 = board.Board()
        squid1 = Squid([(3,3),(3,4)])
        board1.addSquid(squid1)
        board1.fire((3,3))
        
        board2 = board.Board()
        squid2 = Squid([(0,0), (0,1)])
        board2.addSquid(squid2)
        board2.fire((0,0))

        board3 = board.Board()
        squid3 = Squid([(3,3),(3,4)])
        board3.addSquid(squid3)
        board3.fire((2,3))
        board3.fire((3,3))

        board4 = board.Board()
        squid4 = Squid([(6,0), (6,1)])
        board4.addSquid(squid4)
        board4.fire((6,0))
        board4.fire((5,0))

        # WHEN
        destroy = Destroy((3,3))
        move = destroy.findNextMove(board1)

        destroy2 = Destroy((0,0))
        move2 = destroy2.findNextMove(board2)

        destroy3 = Destroy((3,3))
        move3 = destroy3.findNextMove(board3)

        destroy4 = Destroy((6,0))
        move4 = destroy4.findNextMove(board4)

        # THEN
        self.assertTrue(move in [(2,3), (4,3), (3,2), (3,4)], "When detecting a hit the algorithm did not fire on a neighbour")
        self.assertTrue(move2 in [(0,1), (1,0)], "When detecting a hit the algorithm did not fire on a neighbour")
        self.assertTrue(move3 in [(4,3), (3,2), (3,4)], "When detecting a hit the algorithm did not fire on a neighbour")
        self.assertTrue(move4 in [(6,1), (7,0)], "When detecting a hit the algorithm did not fire on a neighbour")


    def test_singleMediumSquidHit(self):
        # GIVEN
        board1 = board.Board()
        squid1 = Squid([(3,3),(3,4),(3,5)])
        board1.addSquid(squid1)
        board1.fire((3,4))
        board1.fire((3,3))
       
        board2 = board.Board()
        squid2 = Squid([(3,3),(3,4),(3,5)])
        board2.addSquid(squid2)
        board2.fire((3,6))
        board2.fire((3,5))
        board2.fire((3,4))

        # WHEN
        destroy1 = Destroy((3,3))
        move1 = destroy1.findNextMove(board1)

        destroy2 = Destroy((3,4))
        move2 = destroy2.findNextMove(board2)

        # THEN
        self.assertTrue(move1 in [(3,5), (3,2)], "When detecting two hits in a straight line the algorithm did not continue firing along that line")
        self.assertEqual(move2, (3,3), "When detecting two hits and a miss in a line, the algorithm did not search in the other direction")

    def test_twoSquidSmallSquidSideBySide(self):
        # GIVEN
        board1 = board.Board()
        squid1 = Squid([(3,3),(3,4)])
        squid2 = Squid([(4,3),(4,4)])
        board1.addSquid(squid1)
        board1.addSquid(squid2)
        board1.fire((3,3))
        board1.fire((4,3))
        board1.fire((5,3))
        board1.fire((2,3))

        board2 = board.Board()
        squid3 = Squid([(6,3),(6,4)])
        squid4 = Squid([(7,3),(7,4)])
        board2.addSquid(squid3)
        board2.addSquid(squid4)
        board2.fire((6,3))
        board2.fire((7,3))
       
        # WHEN
        destroy1 = Destroy((4,3))
        move1 = destroy1.findNextMove(board1)
        board1.fire((3,4))
        move2 = destroy1.findNextMove(board1)
        board1.fire((4,2))
        move3 = destroy1.findNextMove(board1)

        destroy2 = Destroy((6,3))
        destroy2.findNextMove(board2)

        # THEN
        self.assertTrue(move1 in [(3,2), (3,4), (4,2), (4,4)], "When detecting two hits in a straight line with misses on either side that did not kill any squid, the algorithm did not assume that there were two squid side by side and started finishing both")
        self.assertTrue(move2 in [(4,2), (4,4)], "When detecting two hits in a straight line with misses on either side that did not kill any squid, the algorithm did not assume that there were two squid side by side and started finishing both")
        self.assertTrue(move3 in [(4,4)], "When detecting two hits in a straight line with misses on either side that did not kill any squid, the algorithm did not assume that there were two squid side by side and started finishing both")


if __name__ == "__main__":
    unittest.main()
