class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [[0] * N for _ in range(M)]
        dp[M-1][N-1] = grid[M-1][N-1]
        for j in range(N-2, -1, -1):
            dp[M-1][j] = grid[M-1][j] + dp[M-1][j+1]
        
        # Last column
        for i in range(M-2, -1, -1):
            dp[i][N-1] = grid[i][N-1] + dp[i+1][N-1]

        for i in range(M-2, -1, -1):
            for j in range(N-2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j + 1])
        return dp[0][0]