class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSet = {}
        for i in range(len(nums)):
            if nums[i] in numsSet:
                return [numsSet[nums[i]], i]
            else:
                val = target - nums[i]
                numsSet[val] = i 
