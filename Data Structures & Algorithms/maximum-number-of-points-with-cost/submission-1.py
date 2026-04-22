class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])
        prevRow = points[0]

        for r in range(1, ROWS):
            curRow = points[r].copy()
            left, right = [0] * COLS, [0] * COLS
            left[0] = prevRow[0]
            for i in range(1, COLS):
                left[i] = max(prevRow[i], left[i-1] - 1)
            right[COLS - 1] = prevRow[COLS - 1]
            for i in range(COLS - 2, -1, -1):
                right[i] = max(prevRow[i], right[i + 1] - 1)
            for i in range(COLS):
                curRow[i] += max(left[i], right[i])
            prevRow = curRow
        return max(prevRow)
