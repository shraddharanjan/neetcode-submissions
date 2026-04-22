class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visit = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or grid[r][c] == 0:
                return 0 
            visit.add((r,c))
            area = 1
            for dr, dc in directions:
                nx, ny = dr + r, dc + c
                area += dfs(nx, ny)
            return area
            
        maxIsland = 0 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    maxIsland = max(maxIsland, dfs(r,c))

        return maxIsland

        