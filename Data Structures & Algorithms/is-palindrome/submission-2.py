class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        
        l, r = 0, len(s) - 1
        while l < r:  # Only compare while l is less than r
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True





