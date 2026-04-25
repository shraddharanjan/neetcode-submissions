class Solution:
    def findPermutation(self, s: str) -> List[int]:
        res = [0] * (len(s) + 1)
        stack = []
        j = 0

        for i in range(1, len(s) + 1):
            if s[i - 1] == 'I':
                stack.append(i)
                while stack:
                    res[j] = stack.pop()
                    j += 1
            else:
                stack.append(i)

        stack.append(len(s) + 1)
        while stack:
            res[j] = stack.pop()
            j += 1

        return res