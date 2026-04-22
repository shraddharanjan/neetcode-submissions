class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_happy = sum(c for c, g in zip(customers, grumpy) if g == 0)

        extra_happy = 0
        max_extra = 0
        L = 0
        
        for R in range(len(customers)):
            if grumpy[R] == 1:
                extra_happy += customers[R]
            
            if R - L + 1 > minutes:
                if grumpy[L] == 1:
                    extra_happy -= customers[L]
                L += 1
            
            max_extra = max(max_extra, extra_happy)
        
        return total_happy + max_extra
