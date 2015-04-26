from collections import Counter

class Squid:
    def __init__(self, positions):
        assert isinstance(positions, list)

        self.positions = positions

    def __eq__(self, other):
        return Counter(self.positions) == Counter(other.positions)

    def __ne__(self, other):
        return not self.__eq__(other)

    def contains(self, pos):
        assert isinstance(pos, tuple), "Invalid parameter type"

        return pos in self.positions

