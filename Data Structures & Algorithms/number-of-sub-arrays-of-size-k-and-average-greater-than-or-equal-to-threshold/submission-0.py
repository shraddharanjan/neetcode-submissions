class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        res = 0 
        sum = 0 
        for r in range(len(arr)):
            sum += arr[r]
            if r - l + 1 > k:
                sum -= arr[l]
                l += 1

            if r - l + 1 == k:
                average = sum / k 
                if average >= threshold:
                    res += 1

        return res