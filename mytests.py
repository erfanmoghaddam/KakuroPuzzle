import unittest
import sys
import random
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, RIGHT
from View.kakuroUI import KakuroUI
from Model.kakuro import KakuroRandomGame

# unittest requires us to put our tests into classes as methods

game = KakuroRandomGame()
root = Tk()

class Test(unittest.TestCase):

	def test_kakuroUI(self):
		self.main = KakuroUI(root, game)

	def test_kakuroRandomGame(self):
		self.main = game


if __name__ == '__main__':
    unittest.main()
		