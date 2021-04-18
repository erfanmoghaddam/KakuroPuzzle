import sys
import random

class KakuroRandomGame(object):
    """
    Random Kakuro game: Starts a random kakuro game, based on puzzles that have already been stored inside savedpuzzles.txt.
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



class KakuroCustomGame(object):
    """
    Custom Kakuro game: Starts a custom kakuro game, based on the players input.
    """
    def __init__(self):
        self.played_so_far = []
        self.data_filled = []
        self.data_fills = []
        self.data_totals = []
        print 'Enter 9 lines of puzzle.'
        try:
            for i in xrange(9):
                text = raw_input()
                proced = [ele.split('\\') for ele in text.split(',')]
                if len(proced)!=9:
                    raise KakuroError('Nine cells a line or else format not followed!\n')
                for j in xrange(9):
                    if len(proced[j]) == 1 and proced[j][0] == ' ':
                        self.data_fills = self.data_fills + [[i,j]]
                    elif len(proced[j]) == 2:
                        if proced[j][0]!=' ':
                            self.data_totals = self.data_totals + [[int(proced[j][0]),'v',i,j]]
                        if proced[j][1]!=' ':
                            self.data_totals = self.data_totals + [[int(proced[j][1]),'h',i,j]]
        except(ValueError):
            raise KakuroError('Format not followed! Integers only. Check readme.txt for puzzle sample.')
        print '\nStarting custom game. Click on the grid to begin.'
        self.gameId = 0
        self.game_over = False
