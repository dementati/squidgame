import unittest
from ..src.squid import *

class SquidTest(unittest.TestCase):

    def test_equality(self):
        # GIVEN
        squid1 = Squid([(0,0), (1,0)])
        squid2 = Squid([(1,0), (0,0)])

        # THEN
        self.assertEqual(squid1, squid2, "Equal squid indicated as not equal")

    def test_inequality(self):
        # GIVEN
        squid1 = Squid([(0,0), (1,0)])
        squid2 = Squid([(1,0), (2,0)])

        # THEN
        self.assertNotEqual(squid1, squid2, "Unequal squid indicated as equal")
        self.assertNotEqual(squid1, None, "Squid indicated as equal to None")

    def test_containment(self):
        # GIVEN 
        squid = Squid([(0,0), (1,0)])
        containedPosition = (0,0)
        nonContainedPosition = (2,0)

        # WHEN/THEN
        self.assertTrue(squid.contains(containedPosition), "Contained position indicated as not contained")
        self.assertFalse(squid.contains(nonContainedPosition), "Non-contained position indicated as contained")

    def test_overlap(self):
        squid1 = Squid([(0,0), (1,0)])
        squid2 = Squid([(0,0), (0,1)])
        squid3 = Squid([(3,3), (3,4)])

        self.assertTrue(squid1.overlapsWith(squid2), "Squid indicated as not overlapping when they are")
        self.assertFalse(squid1.overlapsWith(squid3), "Squid indicated as overlapping when they are not")

    
if __name__ == "__main__":
    unittest.main()
