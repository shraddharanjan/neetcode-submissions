class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        numMap = {'6': '9', '0': '0', '9': '6', '8': '8', '1': '1'}
        i, j = 0, len(num) - 1
        while i <= j:
            if num[i] not in numMap or numMap[num[i]] != num[j]:
                return False
            i += 1
            j -= 1
        return True