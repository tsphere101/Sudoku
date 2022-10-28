class BoardException:
    @staticmethod
    def size_undefined():
        raise ValueError("Size of table is undefined.")

    @staticmethod
    def size_already_defined():
        raise ValueError("Size of table is already defined.")

    @staticmethod
    def size_invalid(s):
        raise ValueError(f"{s} is invalid table size.")

    @staticmethod
    def index_out_of_bound(index):
        raise IndexError(f"cell {index} is out of bound.")

    @staticmethod
    def non_square():
        raise ValueError("Matrix shape must be square.")

    @staticmethod
    def size_invalid(s):
        raise ValueError(f"{s} is invalid board size.")