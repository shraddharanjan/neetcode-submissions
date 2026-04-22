class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedMap = Counter(allowed)
        count = 0 
        for word in words:
            isAllowed = True
            for c in word:
                if c not in allowedMap:
                    isAllowed = False
                    break 
            if isAllowed:
                count += 1
        return count 

                
                