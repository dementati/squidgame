import copy
from ..squid import Squid

class Board:
    def __init__(self):
        self.squidLengths = [2, 3, 4]
        self.board = [[False for x in range(8)] for x in range(8)]
        self.countPlacementsOnBoard()

    def checked(self, (x,y)):
        return self.board[x][y]

    def check(self, (x,y)):
        self.board[x][y] = True
        self.countPlacementsOnBoard()

    def uncheck(self, (x,y)):
        self.board[x][y] = False
        self.countPlacementsOnBoard()

    def outOfBounds(self, (x,y)):
        return x < 0 or x > 7 or y < 0 or y > 7

    def countPlacementsOnPosition(self, (x, y), squidLength):
        for axis in ["x", "y"]:
            for start in range(-squidLength+1, 1):
                squid = Squid()
                complete = True
                for i in range(squidLength):
                    if axis == "x":
                        pos = (x + start + i, y)
                    else:
                        pos = (x, y + start + i)

                    if self.outOfBounds(pos) or self.checked(pos):
                        complete = False
                        break
                    else:
                        squid.placements.append(pos)
                
                if complete:
                    if not squid in self.placements:
                        self.placements.append(squid)

    def countRemovablePlacements(self, pos):
        count = 0
        for squid in self.placements:
            if squid.contains(pos):
                count += 1

        return count

    def countPlacementsOnBoard(self):
        self.placements = []
        for y in range(8):
            for x in range(8):
                pos = (x,y)
                for squidLength in self.squidLengths:
                    self.countPlacementsOnPosition(pos, squidLength)

        self.dirty = False
        return len(self.placements)

    def findBestMove(self):
        bestMove = None
        bestReduction = 0

        for y in range(8):
            for x in range(8):
                pos = (x,y)
                if not self.checked(pos):
                    reduction = self.countRemovablePlacements(pos)
                    if reduction > bestReduction:
                        bestMove = pos
                        bestReduction = reduction
        
        return bestMove, bestReduction

    def findBestPath(self, moves):
        temp = copy.deepcopy(self)
        for i in range(moves):
            bm, br = temp.findBestMove()
            print(str(bm) + ", " + str(br))
            temp.check(bm)
