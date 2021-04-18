# KakuroPuzzle
Kakuro is a logic puzzle that is often referred to as a mathematical transliteration of the crossword, and we have tried to recreate this classic japanese puzzle in python using 'tkinter', you can also register/login as a player!


# Requirements
Python 2.7<br>
Tkinter GUI toolkit<br>
Pulp modeler - https://pypi.org/project/PuLP/<br>
GLPK module - https://en.wikibooks.org/wiki/GLPK/Python  <br>


#Note
Kakuro Custom Mode:

- Every row of the puzzle is to be entered in a new line. Thus, there should be nine lines terminated by newlines.
- For a row, each cell entry must be delimited by commas. Thus there should be nine cells (and eight commas) a line.
- A blank cell for user input is to be represented by a space character. A darkened cell (with a diagonal partition)
  is to be represented by x\y where x denotes the entry in the lower-left triangular subcell and y denotes the entry
  in the upper-right triangular subcell. x and y can be integers or space character.

sample:
 \ ,16\ ,23\ , \ ,34\ ,16\ ,17\ ,15\ , \ 
 \15, , , \30, , , , , \ 
 \16, , ,17\22, , , , ,4\ 
 \ , \24, , , ,35\ , \8, , 
 \ ,17\ ,30\23, , , ,16\4, , 
 \17, , , \24, , , ,24\ , \ 
 \16, , ,17\ ,16\23, , , ,17\ 
 \ , \29, , , , , \16, , 
 \ , \30, , , , , \17, ,

