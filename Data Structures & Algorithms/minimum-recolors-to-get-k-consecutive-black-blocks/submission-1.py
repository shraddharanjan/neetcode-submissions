class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        L = 0
        count = 0 
        minCount = float('inf') 
        for R in range(len(blocks)):
            if R - L + 1 > k: 
                if blocks[L] == "W":
                    count -= 1
                L += 1
            if blocks[R] == "W":
                count += 1
            if R - L + 1 == k:
                minCount = min(minCount, count)
        return minCount

