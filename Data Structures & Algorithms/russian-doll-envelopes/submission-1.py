class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            LIS = [1] * n

            for i in range(n - 1, -1, -1):
                for j in range(i + 1, n):
                    if nums[i] < nums[j]:
                        LIS[i] = max(LIS[i], 1 + LIS[j])
            return max(LIS)

        return lis([e[1] for e in envelopes])