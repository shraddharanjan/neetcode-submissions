class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing, decreasing = True, True
        for i in range(len(nums) - 1):
            if not (nums[i] <= nums[i + 1]):
                increasing = False
            if not (nums[i] >= nums[i + 1]):
                decreasing = False
        return increasing or decreasing

        
                