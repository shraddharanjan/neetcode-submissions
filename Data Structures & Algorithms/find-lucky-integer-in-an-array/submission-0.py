class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = defaultdict(int)
        res = -1

        for num in arr:
            count[num] += 1
        for key, val in count.items():
            if key == val:
                res = max(res, key)
        return res 
        