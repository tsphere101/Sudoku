from sudoku import Sudoku
from board.board import SudokuBoard
from board.board import Cell
from solver import Solver

# table_size = input("Sudoku Table Generator, please input the size of the table : ")
# difficulty = input("Difficulty (0 to 1) ")

# data = [[1,None],[None,4]]
# data = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
data = [[None,None,1,None],
        [None,None,4,None],
        [None,3,None,None],
        [None,1,None,None]]

# x = None
# data = [
#         [4,x,x,x,x,x,7,x,x],
#         [x,9,x,1,x,x,x,x,x],
#         [x,x,3,x,x,9,6,x,8],
#         [x,x,2,x,x,x,x,1,x],
#         [6,x,x,5,x,x,8,x,2],
#         [x,x,x,x,x,8,x,7,x],
#         [x,x,6,x,x,1,9,x,3],
#         [x,x,x,x,x,x,x,2,x],
#         [5,x,x,x,4,x,x,x,x],
# ]

# s = 4
# for i in range(s):
#     l = []
#     for j in range(s):
#         l.append(j+1)
#     data.append(l)
# print(data)

board = SudokuBoard(data=data)
solver = Solver(board)
# print(board.is_complete())
print(solver.solve())

# print(solver.possible_ans_of_all_empty_cell(board))
# print(solver.solve())

# print(solver.solve())

# Todo
# solver 
# implement board slicing
# generator (solver is required to implement generator)