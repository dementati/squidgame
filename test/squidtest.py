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

    def test_containment(self):
        # GIVEN 
        squid = Squid([(0,0), (1,0)])
        containedPosition = (0,0)
        nonContainedPosition = (2,0)

        # WHEN/THEN
        self.assertTrue(squid.contains(containedPosition), "Contained position indicated as not contained")
        self.assertFalse(squid.contains(nonContainedPosition), "Non-contained position indicated as contained")

if __name__ == "__main__":
    unittest.main()
