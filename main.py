# Python version: 3.6


import sys
import random
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, RIGHT


MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9


class KakuroUI(Frame):
    """
    The Tkinter UI: draw the board and accept input
    """
    def __init__(self, parent, game):
        self.game = game
        Frame.__init__(self, parent)
        self.parent = parent
        self.row, self.col = -1, -1
        self.initUI()

    def initUI(self):
        if self.game.gameId != 0:
            self.parent.title("Kakuro | Puzzle: "+str(self.game.gameId))
        else:
            self.parent.title("Kakuro | Puzzle: Custom")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self, width=WIDTH, height=HEIGHT, highlightthickness=0)
        self.canvas.pack(fill=BOTH, side=TOP)
        clear_button = Button(self, text="Clear answers", command=self.clear_answers)
        clear_button.pack(side=RIGHT)

        self.draw_grid()
        self.draw_puzzle()

        self.canvas.bind("<Button-1>", self.cell_clicked)
        self.canvas.bind("<Up>", self.Upkey_pressed)
        self.canvas.bind("<Down>", self.Downkey_pressed)
        self.canvas.bind("<Right>", self.Rightkey_pressed)
        self.canvas.bind("<Left>", self.Leftkey_pressed)
        self.canvas.bind("<BackSpace>", self.Bkspkey_pressed)
        self.canvas.bind("<Key>", self.key_pressed)

    def draw_grid(self):
        for i in range(10):
            stretch = 0
            if i % 9 == 0:
                stretch = 1
            self.canvas.create_line(
                MARGIN + i * SIDE, MARGIN - stretch,
                MARGIN + i * SIDE, HEIGHT - MARGIN + stretch,
                width=2
            )

            self.canvas.create_line(
                MARGIN, MARGIN + i * SIDE,
                        WIDTH - MARGIN, MARGIN + i * SIDE,
                width=2
            )

        for i in range(9):
            for j in range(9):
                if [i, j] not in self.game.data_fills:
                    self.canvas.create_rectangle(MARGIN + j * SIDE + 1, MARGIN + i * SIDE + 1,
                                                 MARGIN + j * SIDE + SIDE - 2, MARGIN + i * SIDE + SIDE - 2,
                                                 outline="gray", fill="gray", tag = "grays")
                    self.canvas.create_line(
                        MARGIN + j * SIDE, MARGIN + i * SIDE,
                        MARGIN + j * SIDE + SIDE, MARGIN + i * SIDE + SIDE,
                        width=2, tag = "grayliners"
                    )

    def draw_puzzle(self):
        self.canvas.delete("numbersfilled")
        for elem in self.game.data_totals:
            i = elem[2]
            j = elem[3]
            if elem[1] == 'v':
                modif = -1
            else:
                modif = 1
            self.canvas.create_text(
                MARGIN + j * SIDE + SIDE / 2 + modif * SIDE / 4,
                MARGIN + i * SIDE + SIDE / 2 + (-modif) * SIDE / 4,
                text=elem[0], tags="numbers",
                fill="black"
            )
        for elem in self.game.data_filled:
            i = elem[0]
            j = elem[1]
            self.canvas.create_text(
                MARGIN + j * SIDE + SIDE / 2,
                MARGIN + i * SIDE + SIDE / 2,
                font=("Purissa", 20),
                text=elem[2], tags="numbersfilled",
                fill="slate gray"
            )

    def draw_cursor(self):
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            self.canvas.create_rectangle(
                MARGIN + self.col * SIDE + 1,
                MARGIN + self.row * SIDE + 1,
                MARGIN + (self.col + 1) * SIDE - 1,
                MARGIN + (self.row + 1) * SIDE - 1,
                outline="red", tags="cursor"
            )

    def create_circs(self, addrs):
        if len(addrs)==0:
            return
        for elem in addrs:
            self.canvas.create_oval(
                # Figure out the inversion!
                MARGIN + SIDE * elem[1], MARGIN + SIDE * elem[0],
                MARGIN + SIDE * elem[1] + SIDE, MARGIN + SIDE * elem[0] + SIDE,
                tags="circ", outline="red", width=2.0
            )


    def cell_clicked(self, event):
        if self.game.game_over:
            return
        x, y = event.x, event.y
        if (x > MARGIN and x < WIDTH - MARGIN and
                y > MARGIN and y < HEIGHT - MARGIN):
            self.canvas.focus_set()
            row, col = (y - MARGIN) / SIDE, (x - MARGIN) / SIDE
            self.row, self.col = row, col
        else:
            self.row, self.col = -1, -1
        self.draw_cursor()

    def road(self, addr):
        if bool(addr[0] == self.row) == bool(addr[1] == self.col):
            return False
        elif addr[0] == self.row:
            curr_row = self.row
            for iter in range(min(addr[1],self.col), max(addr[1],self.col)):
                if [curr_row, iter] not in self.game.data_fills:
                    return False
            return True
        else:
            curr_col = self.col
            for iter in range(min(addr[0],self.row), max(addr[0],self.row)):
                if [iter, curr_col] not in self.game.data_fills:
                    return False
            return True

    def key_pressed(self, event):
        self.canvas.delete("victory")
        self.canvas.delete("circ")
        if self.game.game_over:
            return
        if self.row >= 0 and self.col >= 0 and event.char in "123456789" and event.char!='' and [self.row, self.col] in self.game.data_fills:
            found_flag = False
            for ind, item in enumerate(self.game.data_filled):
                if item[0]==self.row and item[1]==self.col:
                    found_flag = True
                    self.game.data_filled[ind][2] = int(event.char)
            if(not found_flag):
                self.game.data_filled = self.game.data_filled + [[self.row, self.col, int(event.char)]]

            circlists = []
            for elem in self.game.data_filled:
                if self.road(elem) and elem[2]==int(event.char):
                    if [self.row, self.col] not in circlists:
                        circlists = circlists + [[self.row, self.col]]
                    if [elem[0], elem[1]] not in circlists:
                        circlists = circlists + [[elem[0], elem[1]]]
            self.create_circs(circlists)
            self.draw_puzzle()
            self.draw_cursor()
            if self.game.check_win():
                self.draw_victory()

    def Upkey_pressed(self, event):
        if self.game.game_over:
            return
        if self.row > 0 and self.col >= 0:
            self.row = self.row - 1
            self.draw_cursor()

    def Downkey_pressed(self, event):
        if self.game.game_over:
            return
        if self.row >= 0 and self.col >= 0 and self.row < 8:
            self.row = self.row + 1
            self.draw_cursor()

    def Rightkey_pressed(self, event):
        if self.game.game_over:
            return
        if self.row >= 0 and self.col >= 0 and self.col <8:
            self.col = self.col + 1
            self.draw_cursor()

    def Leftkey_pressed(self, event):
        if self.game.game_over:
            return
        if self.row >= 0 and self.col > 0:
            self.col = self.col - 1
            self.draw_cursor()

    def Bkspkey_pressed(self, event):
        self.canvas.delete("circ")
        if self.game.game_over:
            return
        if self.row >=0 and self.col >=0:
            self.game.data_filled = [item for item in self.game.data_filled if item[0]!=self.row or item[1]!=self.col]
        self.draw_cursor()
        self.draw_puzzle()

    def clear_answers(self):
        self.game.data_filled = []
        self.canvas.delete("circ")
        self.draw_puzzle()

    

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
            file = open("savedpuzzles.txt", "r")
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
            print ("Uh-Oh! You have exhausted the puzzle bank! Gather more puzzles!")
            sys.exit()
        print ("There seem to be "+str(numpuzzles)+" unique untried puzzles this session!")
        print ("Randomly picking one...")
        ctr = 0
        currprob = 1.0/(numpuzzles-ctr)
        currguess = random.random()
        while (currguess>currprob and ctr < numpuzzles-1):
            ctr = ctr + 1
            currprob = 1.0 / (numpuzzles-ctr)
            currguess = random.random()
        self.gameId = puzzlebank[ctr]
        print ("Selected puzzle: Number "+str(puzzlebank[ctr])+ ". Click anywhere on the grid to begin...")
        self.played_so_far = self.played_so_far + [self.gameId]
        file = open("savedpuzzles.txt", "r")
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

    def check_win(self):
        if(len(self.data_filled) == len(self.data_fills)):
            for item in self.data_filled:
                if [item[0], item[1]-1] not in self.data_fills:
                    sumexp = -1
                    for elem in self.data_totals:
                        if elem[2] == item[0] and elem[3] == item[1]-1 and elem[1] == 'h':
                            sumexp = elem[0]
                    offset = 0
                    sumact = []
                    while [item[0], item[1]+offset] in self.data_fills:
                        sumact = sumact + [e[2] for e in self.data_filled if e[0] == item[0] and e[1] == item[1]+offset]
                        offset = offset + 1
                    if len(sumact) != len(set(sumact)):
                        return False
                    if sumexp != -1 and sumexp != sum(sumact):
                        return False
            for item in self.data_filled:
                if [item[0]-1, item[1]] not in self.data_fills:
                    sumexp = -1
                    for elem in self.data_totals:
                        if elem[2] == item[0]-1 and elem[3] == item[1] and elem[1] == 'v':
                            sumexp = elem[0]
                    offset = 0
                    sumact = []
                    while [item[0]+offset, item[1]] in self.data_fills:
                        sumact = sumact + [e[2] for e in self.data_filled if e[0] == item[0]+offset and e[1] == item[1]]
                        offset = offset + 1
                    if len(sumact) != len(set(sumact)):
                        return False
                    if sumexp != -1 and sumexp != sum(sumact):
                        return False
            return True
        else:
            return False




if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("Wrong number of arguments! Enter mode (custom or random) to run in as argument.\n"
               "Example Usage: python kakuro.py random to run random puzzles\n"
               "Going forward with random...\n")
        game = KakuroRandomGame()
        root = Tk()
        ui = KakuroUI(root, game)
        root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        root.mainloop()
    elif sys.argv[1]=='random':
        game = KakuroRandomGame()
        root = Tk()
        ui = KakuroUI(root, game)
        root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        root.mainloop()
    else:
        print ("Wrong number or format of arguments! Enter mode (custom or random) to run in as argument.\n"
               "Example Usage: python kakuro.py random to run random puzzles\n"
               "Going forward with random...\n")
        game = KakuroRandomGame()
        root = Tk()
        ui = KakuroUI(root, game)
        root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        root.mainloop()