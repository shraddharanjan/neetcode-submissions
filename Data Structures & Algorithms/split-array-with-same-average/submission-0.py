class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        # len(A) = a, len(B) = b, let a <= b
        # avg(A) = avg(B)
        # sum(A) / a = sum(B) / b = sum(nums) / n
        # sum(A) / a = avg => sum(A) = a * avg
        # sum(A) = a * sum(nums) / n
        # Find if any subset exists with a * sum(nums) / n
        # a is in the range [1, (n//2)]

        total = sum(nums)
        dp = [set() for _ in range(n // 2 + 1)]

        dp[0].add(0)
        for num in nums:
            for a in range(n // 2, 0, -1):
                for prev in dp[a - 1]:
                    dp[a].add(prev + num)

        for a in range(1, n // 2 + 1):
            if (a * total % n == 0) and (a * total // n) in dp[a]:
                return True

        return False