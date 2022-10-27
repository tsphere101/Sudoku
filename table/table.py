from table.table_exception import TableException


class SudokuTable:
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
            raise ValueError("Invalid size, table size must be greater than 1")

        self.size(size)._construct_table()

    def read_matrix(self,data):
        # Check if data is square matrix
        s = len(data)
        for row in data:
            if len(row) != s:
                TableException.non_square()


        # Parse data to table
        table = SudokuTable(size=s)
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
            TableException.size_already_defined()

        return self._set_size(s)

    def _construct_table(self):
        # Construct 2D list size of NxN

        if self._size is None:
            TableException.size_undefined()

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
            TableException.size_invalid(s)
        self._size = s
        return self

    def _check_index_out_of_bound(self, cell):
        if cell[0] >= self.size() or cell[1] >= self.size():
            TableException.index_out_of_bound(cell)

    def __str__(self) -> str:
        s = ""

        if self.size() is None:
            return "[" + "Empty table" + "]"

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

    def row(self, r):
        return self._table[r]

    def col(self, c):
        l = list()
        for i in range(self.size()):
            l.append(self[i, c])
        return l

    def clone(self):
        s = self.size()
        new_table = SudokuTable()
        new_table.size(s)
        for i in range(s):
            for j in range(s):
                new_table[i][j] = self[i][j]
        return new_table
