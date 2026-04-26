class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        stack = []
        max_val = float('-inf')

        for i in nums:
            while stack and stack[-1] > i:
                stack.pop()

            if i > max_val:
                stack.append(i)

            max_val = max(max_val, i)

        return len(stack)
