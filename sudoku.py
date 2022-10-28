from generator.generator import Generator
from board.board import SudokuBoard

# Game class
class Sudoku:
    def __init__(self,size = None) -> None:
        self.board = SudokuBoard(size)

    def generate(self,board_size):
        gen = Generator()
        return gen.generate(board_size)