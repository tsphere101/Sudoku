from __future__ import division
import math
from board.board_exception import BoardException


class SudokuBoard:
    def __init__(self, size=None, data=None):

        if data is not None:
            # print(type(self.read_matrix(data)))
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
                table[i, j] = data[i][j]

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

    def col(self, c):
        l = list()
        for i in range(self.size()):
            l.append(self[i, c])
        return l

    def undone_cell(self) -> Cell:
        s = self.size()
        for i in range(s):
            for j in range(s):
                if self[i,j] is None:
                    return i,j

    def box(self, cell: tuple) -> list:
        """calculate and return all element in the box that the specified cell is in.

        Returns:
            list : element those are inside the box
        """
        try:
            row, col = cell
        except (ValueError, TypeError) as e:
            raise e

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
                inner_list.append(None)
            self._table.append(inner_list)

        return self

    def _set_size(self, s):
        if s < 2:
            BoardException.size_invalid(s)
        self._size = s
        return self

    def _check_index_out_of_bound(self, cell):
        if cell[0] >= self.size() or cell[1] >= self.size():
            BoardException.index_out_of_bound(cell)

    def _valid_board_size(self, s: int):
        if s == 2:
            return True
        return math.sqrt(s) == math.floor(math.sqrt(s))

    def __str__(self) -> str:
        s = ""

        if self.size() is None:
            return "[" + "Empty board" + "]"

        return "\n".join(str(row) for row in self._table)

    def __getitem__(self, cell):

        self._check_index_out_of_bound(cell)

        return self._table[cell[0]][cell[1]]

    def __setitem__(self, cell, value):

        self._check_index_out_of_bound(cell)

        self._table[cell[0]][cell[1]] = value

    def __iter__(self):
        for i in range(self.size()):
            for j in range(self.size()):
                yield self[i, j]

    def clone(self):
        s = self.size()
        new_table = SudokuBoard()
        new_table.size(s)
        for i in range(s):
            for j in range(s):
                new_table[i][j] = self[i][j]
        return new_table
