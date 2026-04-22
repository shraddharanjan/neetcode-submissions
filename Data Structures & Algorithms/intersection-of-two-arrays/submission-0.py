class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Map = Counter(nums1)
        res = []
        for num in nums2:
            if num in nums1Map:
                res.append(num)
        return list(set(res))

