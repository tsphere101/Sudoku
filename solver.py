from board.board import SudokuBoard
from board.board import Cell
from typing import Set
class Solver:
    def __init__(self,board:SudokuBoard=None):
        self.board = board
        self.complete_element_ref = set(Cell(x+1) for x in range(self.board.size()))

    def is_valid(self,cell) -> bool:
        if not self.board[cell.position].is_empty():
            return False

        board = self.board
        ex_box = board.box(cell)
        ex_row = board.row(cell.row)
        ex_column = board.column(cell.column)
        exists = set(ex_box+ex_row+ex_column)

        return cell not in exists

    def availables(self,cell:Cell) -> Set:
        board = self.board
        ex_box = board.box(cell)
        ex_row = board.row(cell.row)
        ex_column = board.column(cell.column)
        exists = set(ex_box+ex_row+ex_column)
        _availables = self.complete_element_ref.difference(exists)
        return _availables
        

    def solve(self):
        board = self.board.clone()
        
        for cell in board.undone_cells():
            _availables = self.availables(cell)

            print('availables',_availables)

            if len(_availables) == 1:
                new_cell = Cell(_availables.pop(),cell.position,board)
                board.put(new_cell)
            elif len(_availables) > 1:
                for each_cell in _availables:
                    new_cell = Cell(each_cell.value,each_cell.position,board) # undone
                    board.put(new_cell)
                    
            elif len(_availables) == 0:
                pass

            print(board)

        return board