class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        temp = []
        for num in nums:
            num = abs(num)
            temp.append(num* num)
        return sorted(temp)