class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = 0
        
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
        
        # l + 1 is the length of unique elements
        return l + 1

