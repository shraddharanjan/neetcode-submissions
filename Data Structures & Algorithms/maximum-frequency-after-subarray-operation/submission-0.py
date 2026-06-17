class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        res = 0
        for num in nums:
            cnt[num] = max(cnt[num], cnt[k]) + 1
            res = max(res, cnt[num] - cnt[k])
        return cnt[k] + res