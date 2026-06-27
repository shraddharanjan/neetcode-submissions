class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        if self.rows == 0:
            return
        self.cols = len(matrix[0])
        self.bit = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        self._buildBIT(matrix)

    def _lsb(self, n: int) -> int:
        return n & (-n)

    def _updateBIT(self, r: int, c: int, val: int) -> None:
        i = r
        while i <= self.rows:
            j = c
            while j <= self.cols:
                self.bit[i][j] += val
                j += self._lsb(j)
            i += self._lsb(i)

    def _queryBIT(self, r: int, c: int) -> int:
        total = 0
        i = r
        while i > 0:
            j = c
            while j > 0:
                total += self.bit[i][j]
                j -= self._lsb(j)
            i -= self._lsb(i)
        return total

    def _buildBIT(self, matrix: List[List[int]]) -> None:
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                self._updateBIT(i, j, matrix[i - 1][j - 1])

    def update(self, row: int, col: int, val: int) -> None:
        old_val = self.sumRegion(row, col, row, col)
        row += 1
        col += 1
        diff = val - old_val
        self._updateBIT(row, col, diff)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1; col1 += 1; row2 += 1; col2 += 1
        a = self._queryBIT(row2, col2)
        b = self._queryBIT(row1 - 1, col1 - 1)
        c = self._queryBIT(row2, col1 - 1)
        d = self._queryBIT(row1 - 1, col2)
        return (a + b) - (c + d)



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
