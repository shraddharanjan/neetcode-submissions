class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for a in range(min(n, limit) + 1):
            if n - a <= 2 * limit:
                res += min(n - a, limit) - max(0, n - a - limit) + 1
        return res