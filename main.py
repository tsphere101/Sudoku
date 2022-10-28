from sudoku import Sudoku
from board.board import SudokuBoard

# table_size = input("Sudoku Table Generator, please input the size of the table : ")
# difficulty = input("Difficulty (0 to 1) ")

data = [[1,None],[None,4]]
s = Sudoku()
table = SudokuBoard(data=data)


print(table)