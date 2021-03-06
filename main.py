import sys
from tkinter import Tk
from Model.kakuro import KakuroRandomGame
from Model.kakuro import KakuroCustomGame
from View.kakuroUI import KakuroUI
from View.login import main_account_screen

MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ("Wrong number of arguments! Enter mode (custom or random) to run in as argument.\n"
               "Choosing random...\n")
        main_account_screen()
        game = KakuroRandomGame()
        root = Tk()
        ui = KakuroUI(root, game)
        root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        root.mainloop()
    elif sys.argv[1]=='random':
        main_account_screen()
        game = KakuroRandomGame()
        root = Tk()
        ui = KakuroUI(root, game)
        root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        root.mainloop()
    elif sys.argv[1]=='custom':
        main_account_screen()
        game = KakuroCustomGame()
        root = Tk()
        ui = KakuroUI(root, game)
        root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        root.mainloop()
    else:
        print ("Choosing random mode to start the game.")
        main_account_screen()
        game = KakuroRandomGame()
        root = Tk()
        ui = KakuroUI(root, game)
        root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        root.mainloop()
