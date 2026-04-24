class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        charMap = defaultdict(int)
        res = 0
        l = 0

        for r in range(len(s)):
            charMap[s[r]] += 1

            while len(charMap) > 2:
                charMap[s[l]] -= 1
                if charMap[s[l]] == 0:
                    del charMap[s[l]]
                l += 1
            
            res = max(res, r - l + 1)
        return res