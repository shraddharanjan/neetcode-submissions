class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good = -1000
        for i in range(len(num)-2):
            if int(num[i]) == int(num[i + 1]) == int(num[i + 2]):
                good = max(good, int(num[i]))
        return str(good)*3 if good >= 0 else ""

