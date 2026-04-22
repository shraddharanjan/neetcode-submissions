class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numMap = Counter(nums)
        res = 0 
        for count in numMap.values():
            res += count * (count - 1) // 2
        return res

