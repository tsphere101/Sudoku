from sudoku import Sudoku
from board.board import SudokuBoard
from board.board import Cell
from solver import Solver

# table_size = input("Sudoku Table Generator, please input the size of the table : ")
# difficulty = input("Difficulty (0 to 1) ")

# data = [[1,None],[None,4]]
# data = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
data = [[None,1,None,None],[1,4,None,None],
        [None,None,2,1],[None,None,None,None]]
# s = 4
# for i in range(s):
#     l = []
#     for j in range(s):
#         l.append(j+1)
#     data.append(l)
# print(data)

board = SudokuBoard(data=data)
solver = Solver(board)
print(board)

print('done')
cell = Cell(2,(0,0))
print(solver.is_valid(cell))
print(type(solver.availables(cell).pop()))
# print(solver.solve())

# Todo
# solver 
# implement board slicing
# generator (solver is required to implement generator)