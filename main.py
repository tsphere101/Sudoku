from sudoku import Sudoku
from board.board import SudokuBoard

# table_size = input("Sudoku Table Generator, please input the size of the table : ")
# difficulty = input("Difficulty (0 to 1) ")

# data = [[1,None],[None,4]]
# data = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
data = []
for i in range(9):
    l = []
    for j in range(9):
        l.append(j+1)
    data.append(l)
print(data)
s = Sudoku()
board = SudokuBoard(data=data)
board[8,8] = 4
print(board)
print(board.box((8,8)))

# Todo
# implement board slicing
# solver 
# generator (solver is required to implement generator)