class Solution:
    def encode(self, s: str) -> str:
        n = len(s)
        dp = [[""] * n for _ in range(n)]

        def collapse(i, j):
            temp = s[i:j + 1]
            pos = (temp + temp).find(temp, 1)
            if pos >= len(temp):
                return temp
            return str(len(temp) // pos) + "[" + dp[i][i + pos - 1] + "]"

        for step in range(1, n + 1):
            for i in range(n - step + 1):
                j = i + step - 1
                dp[i][j] = s[i:j + 1]

                for k in range(i, j):
                    combined = dp[i][k] + dp[k + 1][j]
                    if len(combined) < len(dp[i][j]):
                        dp[i][j] = combined

                collapsed = collapse(i, j)
                if len(collapsed) < len(dp[i][j]):
                    dp[i][j] = collapsed

        return dp[0][n - 1]
