class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * N
        dp[N-1] = 1
        for i in range(M-1, -1, -1):
            for j in range(N - 1, -1, -1):
                if obstacleGrid[i][j]:
                    dp[j] = 0 
                elif j + 1 < N:
                    dp[j] += dp[j + 1]
        return dp[0]

