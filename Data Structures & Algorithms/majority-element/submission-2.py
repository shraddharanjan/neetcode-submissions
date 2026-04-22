class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapCount = defaultdict(int)
        res = maxCount = 0
        for num in nums:
            mapCount[num] += 1
            if maxCount < mapCount[num]:
                res = num
                maxCount = mapCount[num]
        return res