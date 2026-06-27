class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1, n2 = len(nums1), len(nums2)
        pos1 = 0 # first non-negative in nums1
        while pos1 < n1 and nums1[pos1] < 0:
            pos1 += 1

        pos2 = 0 # first non-negative in nums2
        while pos2 < n2 and nums2[pos2] < 0:
            pos2 += 1

        def count(prod):
            cnt = 0

            # negative * negative -> positive
            i, j = 0, pos2 - 1
            while i < pos1 and j >= 0:
                if nums1[i] * nums2[j] > prod:
                    i += 1
                else:
                    cnt += (pos1 - i)
                    j -= 1

            # positive * positive -> positive
            i, j = pos1, n2 - 1
            while i < n1 and j >= pos2:
                if nums1[i] * nums2[j] > prod:
                    j -= 1
                else:
                    cnt += (j - pos2 + 1)
                    i += 1

            # negative * positive -> negative
            i, j = 0, pos2
            while i < pos1 and j < n2:
                if nums1[i] * nums2[j] > prod:
                    j += 1
                else:
                    cnt += (n2 - j)
                    i += 1

            # positive * negative → negative
            i, j = pos1, 0
            while i < n1 and j < pos2:
                if nums1[i] * nums2[j] > prod:
                    i += 1
                else:
                    cnt += (n1 - i)
                    j += 1

            return cnt

        left, right = -10**10, 10**10
        while left <= right:
            mid = (left + right) // 2
            if count(mid) < k:
                left = mid + 1
            else:
                right = mid - 1

        return left