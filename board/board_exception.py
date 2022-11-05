class BoardException:
    @staticmethod
    def size_undefined():
        raise SizeUndefinedError("Size of table is undefined.")

    @staticmethod
    def size_already_defined():
        raise SizeAlreadyDefinedError("Size of table is already defined")

    @staticmethod
    def size_invalid(s):
        raise SizeInvalidError(f"{s} is invalid table size.")

    @staticmethod
    def index_out_of_bound(index):
        raise IndexError(f"cell {index} is out of bound.")

    @staticmethod
    def non_square():
        raise BoardShapeError("Matrix shape must be square.")

class SizeUndefinedError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class SizeAlreadyDefinedError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class SizeInvalidError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class BoardShapeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)