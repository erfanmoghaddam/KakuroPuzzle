# KakuroPuzzle
Kakuro is a logic puzzle that is often referred to as a mathematical transliteration of the crossword, and we have tried to recreate this classic Japanese puzzle in Python using Tkinter, Pulp and GLPK.<br>

As a player in our game, you can register a new account with your username and password and log in to it. Once the player has successfully logged in, a 9x9 random or custom (based on your input when you start the app) puzzle will be displayed. The player has the chance to enter their answers on the grid, clear answers, try new puzzles and see answers using the built-in solver.<br>

Kakuro is played on a rectangular grid of cells. The aim is to place numbers from 1 to 9 in clocks of empty cells running horizontally and vertically inside the grid. The sum of each block should match the target number, which appears inside darkened cells, divided into two by diagonal lines, at the top (for vertical problems) or to the left (for horizontal ones) of each empty block. No number may be used more than once in each block, or the game will display error.

# Requirements
Python 2.7<br>
Tkinter GUI toolkit<br>
Pulp modeler - https://pypi.org/project/PuLP/<br>
GLPK package - https://www.gnu.org/software/glpk/  <br>


# Note
Kakuro Custom Mode:<br><br>
- Every row of the puzzle is to be entered in a new line. Thus, there should be nine lines terminated by newlines.<br>
- For a row, each cell entry must be delimited by commas. Thus there should be nine cells (and eight commas) a line.<br>
- A blank cell for user input is to be represented by a space character. A darkened cell (with a diagonal partition)<br>
  is to be represented by x\y where x denotes the entry in the lower-left triangular subcell and y denotes the entry<br>
  in the upper-right triangular subcell. x and y can be integers or space character.<br>
sample:<br>
 \ ,16\ ,23\ , \ ,34\ ,16\ ,17\ ,15\ , \ <br>
 \15, , , \30, , , , , \ <br>
 \16, , ,17\22, , , , ,4\ <br>
 \ , \24, , , ,35\ , \8, , <br>
 \ ,17\ ,30\23, , , ,16\4, , <br>
 \17, , , \24, , , ,24\ , \ <br>
 \16, , ,17\ ,16\23, , , ,17\ <br>
 \ , \29, , , , , \16, , <br>
 \ , \30, , , , , \17, ,<br>

