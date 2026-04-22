class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            num = numbers[r] + numbers[l] 
            if num == target:
                return [l + 1, r + 1]
            elif num > target:
                r -= 1
            else:
                l += 1