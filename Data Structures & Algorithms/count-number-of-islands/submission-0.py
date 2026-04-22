class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        islands = 0 

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            for dx, dy in directions:
                dfs(dx + r, dy + c)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        return islands
            