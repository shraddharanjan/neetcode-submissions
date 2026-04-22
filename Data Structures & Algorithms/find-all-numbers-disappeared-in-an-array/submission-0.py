class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        store = set(range(1, len(nums) + 1))
        for num in nums:
            store.discard(num)

        return list(store)
