class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        textMap = {}
        balloonText = {"b": 1, "a":1, "l":2, "o":2, "n": 1}
        res = len(text)
        for c in text:
            textMap[c] = 1 + textMap.get(c, 0)
        for c in balloonText:
            res = min(res, textMap.get(c, 0) // balloonText[c])
        return res        
            