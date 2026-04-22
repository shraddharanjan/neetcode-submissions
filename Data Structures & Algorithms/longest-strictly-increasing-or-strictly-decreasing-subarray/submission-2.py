class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incCount, decCount = 1, 1
        maxCount = 1 
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                incCount += 1
                maxCount = max(incCount, maxCount)
                decCount = 1 
            elif nums[i] < nums[i - 1]:
                decCount += 1
                maxCount = max(decCount, maxCount)
                incCount = 1
            else:
                incCount = 1 
                decCount = 1
                maxCount = max(incCount, decCount, maxCount)
        return maxCount




            