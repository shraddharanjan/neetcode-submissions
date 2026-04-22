class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) -1, -1, -1):
            newDp = [0] * (amount + 1)
            newDp[0] = 1
            for a in range(1, amount + 1):
                newDp[a] = dp[a]
                if a - coins[i] >= 0:
                    newDp[a] += newDp[a - coins[i]]
            dp = newDp 
        return dp[amount]