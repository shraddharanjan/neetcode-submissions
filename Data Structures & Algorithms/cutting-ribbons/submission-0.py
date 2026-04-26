class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        left = 0 
        right = max(ribbons)

        while left < right:
            middle = (left + right + 1) // 2
            if self.is_possible(middle, ribbons, k):
                left = middle
            else:
                right = middle - 1
        return left 
    def is_possible(self, x: int, ribbons: list[int], k: int) -> bool:
        total_ribbons = 0
        for ribbon in ribbons:
            total_ribbons += ribbon // x
            if total_ribbons >= k:
                return True
        return False