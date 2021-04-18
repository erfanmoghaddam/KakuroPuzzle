# KakuroPuzzle
Kakuro is a logic puzzle that is often referred to as a mathematical transliteration of the crossword, and we have tried to recreate this classic japanese puzzle in python using 'tkinter', you can also register/login as a player!


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

