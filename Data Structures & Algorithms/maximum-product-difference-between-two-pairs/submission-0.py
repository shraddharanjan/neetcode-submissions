class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        cd = nums[0] * nums[1]
        ab = nums[len(nums) - 1] * nums[len(nums) - 2]
        return ab - cd