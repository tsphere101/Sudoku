from board.board import SudokuBoard
from board.board import Cell
from typing import Set, List


class Solver:
    def __init__(self, board: SudokuBoard = None):
        self.board = board
        self.complete_element_ref = set(x+1 for x in range(self.board.size()))
        # self.complete_element_ref = set(Cell(x+1)
        #                                 for x in range(self.board.size()))

    def is_valid(self, cell) -> bool:
        if not self.board[cell.position].is_empty():
            return False

        board = self.board
        ex_box = board.box(cell)
        ex_row = board.row(cell.row)
        ex_column = board.column(cell.column)
        exists = set(ex_box+ex_row+ex_column)

        return cell not in exists

    def availables(self, cell: Cell) -> Set:
        board = self.board
        ex_box = [e.value for e in board.box(cell)]
        ex_row = [e.value for e in board.row(cell.row)]
        ex_column = [e.value for e in board.column(cell.column)]
        exists = ex_box+ex_row+ex_column
        exists = set(dict.fromkeys(e for e in (exists)))
        _availables = self.complete_element_ref.difference(exists)
        return _availables

    def possible_ans_of_all_empty_cell(self,board:SudokuBoard):
        stack = Stack(board)
        solver = Solver(board)

        for cell in board.undone_cells():
            _availables = solver.availables(cell)
            stack.append(PossibleAnswer(_availables,cell))
        
        return stack

    def solve(self):
        board = self.board.clone()

        i = 0
        # print(board.is_complete())
        while not board.is_complete():
            # print("BOARD[2,2] =",board[2,2],type(board[2,2]))
            # print("Solving")

            stack = self.possible_ans_of_all_empty_cell(board)
            lpa = stack.get_least_possible_answer()
            # print(f"choosing {lpa}")

            _v = lpa.pop()
            # print('TTT',type(_v))
            c = Cell(_v,lpa.cell.position,board)
            board.put(c)
            # print(f"value {c.value} has been put to cell {c.position}")

            # print(board)
            # print("===")


        return board


class PossibleAnswer:
    def __init__(self, elements: List, cell: Cell) -> None:
        self.elements = elements
        self.cell = cell

    def __len__(self) -> int:
        return len(self.elements)

    def __repr__(self) -> str:
        return str(self.elements)

    def pop(self):
        return self.elements.pop()


class Stack:
    def __init__(self, board: SudokuBoard) -> None:
        self.l = []
        self.board = board
        self.MOST = board.size()

    def append(self, o: PossibleAnswer):
        self.l.append(o)

    def get_least_possible_answer(self) -> PossibleAnswer:
        least = self.MOST
        result = None
        for e in self.l:
            if len(e) <= least:
                least = len(e)
                result = e

        return result

    def __repr__(self) -> str:
        return str(self.l)