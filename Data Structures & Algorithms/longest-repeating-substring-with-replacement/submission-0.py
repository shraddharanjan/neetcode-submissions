class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        charSet = {}
        res = 0 
        maxf= 0
        for R in range(len(s)):
            charSet[s[R]] = 1 + charSet.get(s[R], 0)
            maxf = max(maxf, charSet[s[R]])
            if (R - l + 1) - maxf > k:
                charSet[s[l]] -= 1
                l += 1
            res = max(res, R - l + 1)
        return res

