class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        patternToWord = {}
        wordToPattern = {}
        
        for p, w in zip(pattern, words):
            if p in patternToWord and patternToWord[p] != w:
                return False
            if w in wordToPattern and wordToPattern[w] != p:
                return False
            
            patternToWord[p] = w
            wordToPattern[w] = p
        
        return True
