class Solution:

    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n = len(coins)
        nxt = [-1] * n
        dp = [0] * n

        for i in range(n - 2, -1, -1):
            min_cost = float('inf')

            for j in range(i + 1, min(i + maxJump + 1, n)):
                if coins[j] >= 0:
                    cost = coins[i] + dp[j]

                    if cost < min_cost:
                        min_cost = cost
                        nxt[i] = j

            dp[i] = min_cost

        res = []
        i = 0
        while i < n and nxt[i] > 0:
            res.append(i + 1)
            i = nxt[i]

        if i == n - 1 and coins[i] >= 0:
            res.append(n)
            return res

        return []
