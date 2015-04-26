class Squid:
    def __init__(self):
        self.placements = []

    def __eq__(self, other):
        return Counter(self.placements) == Counter(other.placements)

    def __ne__(self, other):
        return not self.__eq__(other)

    def contains(self, pos):
        assert isinstance(pos, tuple), "Invalid parameter type"

        return pos in self.placements

