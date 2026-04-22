class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        left_zero = [0] * n
        right_one = [0] * n

        if s[0] == '0':
            left_zero[0] = 1
        for i in range(1, n):
            left_zero[i] = left_zero[i - 1]
            if s[i] == '0':
                left_zero[i] += 1

        if s[n - 1] == '1':
            right_one[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right_one[i] = right_one[i + 1]
            if s[i] == '1':
                right_one[i] += 1

        res = 0
        for i in range(1, n):
            res = max(res, left_zero[i - 1] + right_one[i])
        return res
