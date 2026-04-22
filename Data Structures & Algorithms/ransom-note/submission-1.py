class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineMap = Counter(magazine)
        temp = magazineMap.copy()
        for c in ransomNote:
            if temp[c] <= 0:
                return False
            temp[c] -= 1
        return True 
        
