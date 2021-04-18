import unittest
import sys
import random
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, RIGHT
from View.kakuroUI import KakuroUI
from Model.kakuro import KakuroRandomGame, KakuroCustomGame
from View.login import *


# unittest requires us to put our tests into classes as methods

MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9


# functions
def testKakuroRandomGame():
	game = KakuroRandomGame()
	root = Tk()
	ui = KakuroUI(root, game)
	root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
	root.mainloop()  


def testCustomKakuroGame():
	game = KakuroCustomGame()
	root = Tk()
	ui = KakuroUI(root, game)
	root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
	root.mainloop()


def testGrid():
	root = Tk()
	root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
	root.mainloop()


def testLogin():
	main_account_screen()




class Test(unittest.TestCase):

	# def test_kakuro_random(self):
	# 	self.main = testKakuroRandomGame()

	# def test_kakuro_custom(self):
	#     self.main = testCustomKakuroGame()  

	def test_tkinter(self):
	    self.main = testGrid()

	# def test_login(self):
	# 	self.main = testLogin()



if __name__ == '__main__':
	unittest.main()
		