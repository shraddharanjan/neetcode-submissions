class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones, maxOnes = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
                maxOnes = max(ones, maxOnes)
            else:
                ones = 0 
        return maxOnes

        