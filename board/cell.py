class Cell:
    def __init__(self, value: object = None, position: tuple = None, board: object = None):
        """Smallest unit in Sudoku board

        Args:
            value (object): value in cell, typically natural number
            pos (tuple): row and column position in board
            board (SudokuBoard): Sudoku board that the cell belongs to
        """
        self.value = value
        self.position = position
        self.board = board

    @property
    def row(self) -> int:
        return self.position[0]

    @property
    def column(self) -> int:
        return self.position[1]

    def complete(self):
        pass

    def is_empty(self):
        return self.value == None

    def box(self) -> list:
        """Get all element in the box that the cell in.

        Returns:
            list : Cells those are inside the box
        """
        try:
            row, col = self.position
        except (ValueError, TypeError) as e:
            raise e

        s = self.board.size()
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
                element.append(self.board[r, c])

        return element

    def __repr__(self) -> str:
        return str(self.value)

    def __str__(self)->str:
        return str(self.value)

    def __hash__(self) -> int:
        return hash(self.__repr__())

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o,Cell):
            return __o.value == self.value

        return __o == self.value
