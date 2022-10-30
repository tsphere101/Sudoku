from board import SudokuBoard


class Cell:
    def __init__(self, value: int, pos: tuple, board: SudokuBoard):
        self.value = value
        self.pos = pos
        self.board = board

    def complete(self):
        pass
