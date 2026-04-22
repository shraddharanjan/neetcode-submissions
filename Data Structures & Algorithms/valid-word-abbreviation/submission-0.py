class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n, m  = len(word), len(abbr)
        i, j = 0, 0 
        while i < n and j < m:
            if word[i] == abbr[j]:
                i, j = i + 1, j + 1
            elif abbr[j].isalpha() or abbr[j] == "0":
                return False
            else: 
                subLen = 0
                while j < m and abbr[j].isdigit():
                    subLen = subLen * 10 + int(abbr[j])
                    j += 1
                i += subLen 
        return i == n and j == m 
                
                
