class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1 
        for num in nums:
            temp = curMax * num
            curMax = max(num * curMax, curMin * num, num)
            curMin = min(temp, curMin * num, num)
            res = max(res, curMax)
        return res