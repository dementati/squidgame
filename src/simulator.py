import random
from board import *
from algorithms.movealgorithm import MoveAlgorithm
from squid import Squid
from boardgenerator import BoardGenerator
import logging

class Simulator:

    def __init__(self, runs = 1000):
        self.runs = runs

    def run(self, algorithmFactory, maxMoves = 24):
        assert isinstance(algorithmFactory(), MoveAlgorithm), "Invalid parameter type"

        boardGenerator = BoardGenerator()

        wonGames = 0
        wonGameMoveCount = []
        for i in range(self.runs):
            board = boardGenerator.generate()
            algorithm = algorithmFactory()
           
            for j in range(maxMoves):
                move = algorithm.findNextMove(board)

                assert isinstance(move, tuple), "Algorithm move must be a tuple"
                assert board.getState(move) == State.EMPTY, "Fire target must be empty"

                board.fire(move)

                if board.isWon():
                    logging.debug("The game is won!")
                    break
        
            if board.isWon():
                wonGames += 1
                wonGameMoveCount.append(j)
        
        return wonGames, wonGameMoveCount
