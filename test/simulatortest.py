from __future__ import division
import unittest
from ..src.simulator import Simulator
from ..src.algorithms.randomsearch import RandomSearch
from ..src.algorithms.randomsearchanddestroy import RandomSearchAndDestroy
from ..src.algorithms.placementsubtractionanddestroy import PlacementSubtractionAndDestroy
import logging

def average(l):
    return float(sum(l))/len(l) if len(l) > 0 else float('nan')

def printStatistics(name, wg, wgm, runs, maxMoves=24):
    print
    print "* %s" % name
    print "Won games: %d/%d" % (wg, runs)
    print "Win rate: %.1f %%" % (100 * wg/runs)
    print "Average number of moves per win: %f" % average(wgm)
    print "Average number of moves: %f" % average(wgm + (runs - wg) * [maxMoves])
    print


class SimulatorTest(unittest.TestCase):

    def setUp(self):
        self.runs = 1000
        #logging.basicConfig(level=logging.DEBUG)

    def test_randomSearch(self):
        self.runTest(lambda: RandomSearch(), "RandomSearch")
        pass

    def test_randomSearchAndDestroy(self):
        self.runTest(lambda: RandomSearchAndDestroy(), "RandomSearchAndDestroy")
        pass

    def test_placementSubtractionAndDestroy(self):
        self.runTest(lambda: PlacementSubtractionAndDestroy(), "PlacementSubtractionAndDestroy")
    
    def runTest(self, algorithmFactory, name):
        simulator = Simulator(self.runs)
        wg, wgm = simulator.run(algorithmFactory)
        printStatistics(name, wg, wgm, self.runs)

if __name__ == "__main__":
    unittest.main()
