class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total = 0 
        res = 0 

        for i in range(len(nums)):
            if nums[i - 1] >= nums[i]:
                total = nums[i]
                res = max(total, res)
            else:
                total += nums[i]
                res = max(total, res)
        return res 

