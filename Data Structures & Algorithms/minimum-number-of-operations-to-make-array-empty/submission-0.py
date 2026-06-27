class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0

        for num, cnt in count.items():
            if cnt == 1:
                return -1
            res += math.ceil(cnt / 3)

        return res