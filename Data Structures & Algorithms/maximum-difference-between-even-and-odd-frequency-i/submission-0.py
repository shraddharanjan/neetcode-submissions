class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        oddMax, evenMin = 0, len(s)
        for c in count.values():
            if c & 1:
                oddMax = max(oddMax, c)
            else:
                evenMin = min(evenMin, c)
        return oddMax - evenMin