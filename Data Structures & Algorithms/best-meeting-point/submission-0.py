class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows = self.collectRows(grid)
        cols = self.collectCols(grid)
        return self.minDistance1D(rows) + self.minDistance1D(cols)

    def minDistance1D(self, points: List[int]) -> int:
        distance = 0
        i, j = 0, len(points) - 1
        while i < j:
            distance += points[j] - points[i]
            i += 1
            j -= 1
        return distance

    def collectRows(self, grid: List[List[int]]) -> List[int]:
        rows = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    rows.append(row)
        return rows

    def collectCols(self, grid: List[List[int]]) -> List[int]:
        cols = []
        for col in range(len(grid[0])):
            for row in range(len(grid)):
                if grid[row][col] == 1:
                    cols.append(col)
        return cols
