class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsMap = Counter(chars)
        res = 0 
        for word in words:
            valid = True
            temp = charsMap.copy()
            for w in word:
                if temp[w] == 0:
                    valid = False
                    break 
                temp[w] -= 1
            if valid:
                res += len(word)
        return res
            