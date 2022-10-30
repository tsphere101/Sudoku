import math
from board.board_exception import BoardException
from board.cell import Cell
from typing import List


class SudokuBoard:
    def __init__(self, size: int = None, data: List[List] = None):

        if data is not None:
            read_matrix = self.read_matrix(data)
            self.size(read_matrix.size())._construct_table()
            self._table = read_matrix._table
            return

        if size is None:
            return

        if size <= 1:
            BoardException.size_invalid(size)

        if not self._valid_board_size(size):
            BoardException.size_invalid(size)

        self.size(size)._construct_table()

    def read_matrix(self, data):
        # Check if data is square matrix
        s = len(data)
        for row in data:
            if len(row) != s:
                BoardException.non_square()

        # Parse data to table
        table = SudokuBoard(size=s)
        for i in range(s):
            for j in range(s):
                table[i, j] = Cell(data[i][j], (i, j), self)

        return table

    def size(self, s=None) -> object:
        if s is None:
            if hasattr(self, '_size'):
                return self._size
            return None

        if hasattr(self, '_size'):
            BoardException.size_already_defined()

        return self._set_size(s)

    def row(self, r):
        return self._table[r]

    def column(self, c):
        l = list()
        for i in range(self.size()):
            l.append(self[i, c])
        return l

    def put(self, cell: Cell) -> object:
        if not self[cell.position].is_empty():
            raise ValueError('Cell occupied')
        self[cell.position] = cell
        return self

    def undone_cells(self) -> List[Cell]:
        s = self.size()
        cells = []
        for i in range(s):
            for j in range(s):
                if self[i, j].is_empty():
                    cells.append(self[i, j])
        return cells

    def box(self, cell: Cell) -> list:
        """calculate and return all element in the box that the specified cell is in.

        Returns:
            list : element those are inside the box
        """
        row = cell.row
        col = cell.column

        s = self.size()
        division = 2 if s % 2 == 0 else 3
        box_size = s // division
        r_boxth = row // division
        r_box_lower = r_boxth * box_size  # include
        r_box_upper = (r_boxth+1) * box_size  # exclude

        c_boxth = col // division
        c_box_lower = c_boxth * box_size  # include
        c_box_upper = (c_boxth + 1) * box_size  # exclude

        element = list()
        for r in range(r_box_lower, r_box_upper):
            for c in range(c_box_lower, c_box_upper):
                element.append(self[r, c])

        return element

    def _construct_table(self):
        # Construct 2D list size of NxN

        if self._size is None:
            BoardException.size_undefined()

        size = self._size

        self._table = list()
        for i in range(size):
            inner_list = list()
            for j in range(size):
                inner_list.append(Cell(None, (i, j), self))
            self._table.append(inner_list)

        return self

    def _set_size(self, s):
        if s < 2:
            BoardException.size_invalid(s)
        self._size = s
        return self._construct_table()

    def _check_index_out_of_bound(self, cell):
        if cell[0] >= self.size() or cell[1] >= self.size():
            BoardException.index_out_of_bound(cell)

    def _valid_board_size(self, s: int):
        if s == 2:
            return True
        return math.sqrt(s) == math.floor(math.sqrt(s))

    def __str__(self) -> str:
        if self.size() is None:
            return "[" + "Empty board" + "]"

        return "\n".join(str(row) for row in self._table)

    def __getitem__(self, position):

        self._check_index_out_of_bound(position)

        return self._table[position[0]][position[1]]

    def __setitem__(self, position, value):

        self._check_index_out_of_bound(position)

        self._table[position[0]][position[1]] = value

    def __iter__(self):
        for i in range(self.size()):
            for j in range(self.size()):
                yield self[i, j]

    def clone(self):
        s = self.size()
        new_board = SudokuBoard()
        new_board.size(s)
        for i in range(s):
            for j in range(s):
                new_board[i, j] = Cell(self[i, j].value, (i, j), new_board)
        return new_board
