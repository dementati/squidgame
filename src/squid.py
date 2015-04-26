from collections import Counter

class Squid:
    def __init__(self, positions):
        assert isinstance(positions, list), "Invalid parameter type"
        assert len(positions) > 0, "Squid cannot have zero length"
        

        self.positions = positions
        
        assert Squid.isStraight(self.positions), "Squid must be straight"
        assert Squid.isCoherent(self.positions), "Squid must be coherent"

    @staticmethod
    def isStraight(positions):
        return all([positions[0][0] == pos[0] for pos in positions]) or all([positions[0][1] == pos[1] for pos in positions])

    @staticmethod
    def isCoherent(positions):
        xs = sorted([x for (x,y) in positions])
        ys = sorted([y for (x,y) in positions])

        return xs == range(xs[0], xs[-1]+1) or ys == range(ys[0], ys[-1]+1)

    def __eq__(self, other):
        return Counter(self.positions) == Counter(other.positions)

    def __ne__(self, other):
        return not self.__eq__(other)

    def contains(self, pos):
        assert isinstance(pos, tuple), "Invalid parameter type"

        return pos in self.positions

    def overlapsWith(self, other):
        assert isinstance(other, Squid), "Invalid parameter type"

        return any([i in self.positions for i in other.positions])

    def getPositions(self):
        return self.positions
