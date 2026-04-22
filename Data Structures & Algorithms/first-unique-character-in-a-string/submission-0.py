class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = Counter(s)
        for i, c in enumerate(s):
            if seen[c] == 1:
                return i
        return -1

        