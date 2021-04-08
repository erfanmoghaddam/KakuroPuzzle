import sys
import random

class KakuroRandomGame(object):
    """
    A Kakuro game. Stores gamestate and completes the puzzle as needs be
    """
    def __init__(self):
        self.played_so_far = []
        self.data_filled = []
        self.data_fills = []
        self.data_totals = []
        puzzlebank = []
        try:
            file = open("Controller/savedpuzzles.txt", "r")
        except IOError:
            print("Could not acquire read access to file: savedpuzzles.txt")
            sys.exit()
        with file:
            for line in file:
                if line.rstrip("\r\n").isdigit():
                    puzzlebank = puzzlebank + [int(line)]
            file.close()
        puzzlebank = [ele for ele in puzzlebank if ele not in self.played_so_far]
        numpuzzles = len(puzzlebank)
        if len(puzzlebank) == 0:
            print("Uh-Oh! You have exhausted the puzzle bank! Gather more puzzles!")
            sys.exit()
        print("There seem to be "+str(numpuzzles)+" unique untried puzzles this session!")
        print("Randomly picking one...")
        ctr = 0
        currprob = 1.0/(numpuzzles-ctr)
        currguess = random.random()
        while (currguess>currprob and ctr < numpuzzles-1):
            ctr = ctr + 1
            currprob = 1.0 / (numpuzzles-ctr)
            currguess = random.random()
        self.gameId = puzzlebank[ctr]
        print("Selected puzzle: Number "+str(puzzlebank[ctr])+ ". Click anywhere on the grid to begin...")
        self.played_so_far = self.played_so_far + [self.gameId]
        file = open("Controller/savedpuzzles.txt", "r")
        readstatus = 0
        for line in file:
            if readstatus == 0 and line.rstrip("\r\n").isdigit():
                if int(line) == puzzlebank[ctr]:
                    readstatus = 1
                    continue
            if readstatus == 1 and line.rstrip("\r\n").isdigit():
                break
            elif readstatus == 1:
                line = line.rstrip("\r\n")
                if line[0] == 'e':
                    self.data_fills = self.data_fills + [[int(line[1]), int(line[2])]]
                else:
                    self.data_totals = self.data_totals + [[int(line[:-3]), line[-3], int(line[-2]), int(line[-1])]]
        file.close()
        self.game_over = False
