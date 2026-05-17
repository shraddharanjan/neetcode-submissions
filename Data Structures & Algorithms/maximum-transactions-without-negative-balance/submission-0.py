class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        max_neg_heap = []  # min-heap of negative values (most negative on top)
        balance = 0
        count = 0

        for t in transactions:
            balance += t
            count += 1
            if t < 0:
                heapq.heappush(max_neg_heap, t)

            if balance < 0:
                balance -= heapq.heappop(max_neg_heap)
                count -= 1

        return count
