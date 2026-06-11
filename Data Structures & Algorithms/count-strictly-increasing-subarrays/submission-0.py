class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        currSubarray = 1
        subarrayCount = 1

        for i in range(1, len(nums)):
            # If the current element is greater, increase the subarrays.
            if nums[i] > nums[i - 1]:
                currSubarray += 1
            else:
                # Otherwise, reset the subarray size to 1.
                currSubarray = 1
            # Add the number of subarrays to the total count.
            subarrayCount += currSubarray

        return subarrayCount
