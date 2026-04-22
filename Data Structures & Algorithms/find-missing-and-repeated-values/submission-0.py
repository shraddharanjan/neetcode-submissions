class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        marked = [False] * (n*n + 1)
        a = b = 0

        for row in grid:
            for num in row:
                if marked[num]:
                    a = num
                marked[num] = True

        for i in range(1, n*n + 1):
            if not marked[i]:
                b = i

        return [a, b]