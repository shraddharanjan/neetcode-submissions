class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        prev = [[float("-inf")] * n for _ in range(n)]
        prev[0][0] = grid[0][0]

        for k in range(1, 2 * n - 1):
            dp = [[float("-inf")] * n for _ in range(n)]
            for r1 in range(max(0, k - (n - 1)), min(n, k + 1)):
                c1 = k - r1
                if c1 >= n or grid[r1][c1] == -1:
                    continue
                for r2 in range(max(0, k - (n - 1)), min(n, k + 1)):
                    c2 = k - r2
                    if c2 >= n or grid[r2][c2] == -1:
                        continue
                    val = prev[r1][r2]
                    if r1 > 0: val = max(val, prev[r1 - 1][r2])
                    if r2 > 0: val = max(val, prev[r1][r2 - 1])
                    if r1 > 0 and r2 > 0: val = max(val, prev[r1 - 1][r2 - 1])
                    if val < 0: continue
                    val += grid[r1][c1]
                    if r1 != r2: val += grid[r2][c2]
                    dp[r1][r2] = val
            prev = dp

        return max(0, prev[n - 1][n - 1])