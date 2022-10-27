from table.table import SudokuTable
import random


class Generator:
    def __init__(self, size: int = None) -> None:
        self._diff = 0
        self.size = size

    def difficulty(self, level: float = 0.0) -> object:
        # """
        # Set the difficulty level of the Sudoku table that will be generated.

        # Args:
        #     level (float, optional): Value between 0 to 1. Defaults to 0.

        # Returns:
        #     Generator: self
        # """

        self._diff = level

        return self

    def _bernoulli(self, p: float, k: int = 1):
        return random.choices([1, 0], weights=[p, 1-p], k=k)

    def generate(self, size: int = None) -> SudokuTable:
        # """
        # Generate random Sudoku table with the specified table size

        # Args:
        #     size (int, optional): table size. Defaults to None.

        # Raises:
        #     ValueError: If size is not specified

        # Returns:
        #     SudokuTable: Incomplete Sudoku table.

        # """

        if (size is None) and (self.size is None):
            raise ValueError("Generator size undefined")

        s = size if size is not None else self.size

        table = SudokuTable(size=s)

        for i in range(table.size()):
            for j in range(table.size()):

                table[i, j] = 1 # random.randint(1, size+1)

        return table
