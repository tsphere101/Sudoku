from sudoku import Sudoku
from table.table import SudokuTable

# table_size = input("Sudoku Table Generator, please input the size of the table : ")
# difficulty = input("Difficulty (0 to 1) ")

data = [[1,None],[None,4]]
s = Sudoku()
table = SudokuTable(data=data)

print(table)