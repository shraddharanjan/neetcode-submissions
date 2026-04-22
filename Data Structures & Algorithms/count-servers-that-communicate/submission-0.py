class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        row_count = [0] * ROWS
        col_count = [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    row_count[r] += 1
                    col_count[c] += 1
        
        res = 0 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and max(row_count[r], col_count[c]) > 1:
                    res += 1
        return res

        
