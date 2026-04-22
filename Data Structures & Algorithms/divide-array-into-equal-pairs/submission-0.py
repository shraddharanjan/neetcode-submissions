class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 1:
            return False
        num = sorted(nums)
        i = 0
        while i != len(num):
            if num[i] != num[i + 1]:
                return False
            i += 2
        return True 
        

