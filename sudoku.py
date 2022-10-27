from generator import Generator
from table.table import SudokuTable

# Game class
class Sudoku:
    def __init__(self,size = None) -> None:
        self.table = SudokuTable(size)

    def generate(self,table_size):
        gen = Generator()
        return gen.generate(table_size)