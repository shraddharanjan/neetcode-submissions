class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = sorted(prices)
        total = prices[0] + prices[1]
        return money - total if (money - total) >= 0 else money 