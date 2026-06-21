class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = set(arr2)
        arr1_count = defaultdict(int)
        end = []

        for num in arr1:
            if num not in arr2_set:
                end.append(num)
            arr1_count[num] += 1
        end.sort()

        res = []
        for num in arr2:
            for _ in range(arr1_count[num]):
                res.append(num)
        return res + end