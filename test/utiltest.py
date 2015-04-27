from ..src import util
import unittest

class UtilTest(unittest.TestCase):
    def test_isStraight(self):
        positions1 = [(0,0), (1,0), (2,0)]
        positions2 = [(0,0), (1,0), (1,1)]
        positions3 = [(0,0), (0,1), (0,2)]

        self.assertTrue(util.isStraight(positions1), "Indicated as not straight when it is")
        self.assertFalse(util.isStraight(positions2), "Indicated as straight when it is not")
        self.assertTrue(util.isStraight(positions3), "Indicated as not straight when it is")
        
    def test_isCoherent(self):
        positions1 = [(0,0), (1,0), (2,0)]
        positions2 = [(0,0), (0,1), (0,2)]
        positions3 = [(0,0), (2,0), (3,0)]
        positions4 = [(0,0), (0,2), (0,3)]

        self.assertTrue(util.isCoherent(positions1), "Is indicated as incoherent when it is not")
        self.assertTrue(util.isCoherent(positions2), "Is indicated as incoherent when it is not")
        self.assertFalse(util.isCoherent(positions3), "Is indicated as coherent when it is not")
        self.assertFalse(util.isCoherent(positions4), "Is indicated as coherent when it is not")

if __name__ == "__main__":
    unittest.main()
