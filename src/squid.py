import util
from collections import Counter
import logging

class Squid:
    def __init__(self, positions):
        if positions != []:
            assert isinstance(positions, list), "Invalid parameter type"
            assert len(positions) > 0, "Squid cannot have zero length"
            assert util.isStraight(positions), "Squid must be straight"
            assert util.isCoherent(positions), "Squid must be coherent"

        self.positions = positions

    def __eq__(self, other):
        if other == None:
            return False

        return Counter(self.positions) == Counter(other.positions)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __len__(self):
        return len(self.positions)

    def contains(self, pos):
        assert isinstance(pos, tuple), "Invalid parameter type"

        return pos in self.positions

    def overlapsWith(self, other):
        assert isinstance(other, Squid), "Invalid parameter type"

        return any([i in self.positions for i in other.positions])

    def getPositions(self):
        return self.positions
