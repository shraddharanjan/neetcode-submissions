class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        totalApples = sum(weight)
        if totalApples > 5000:
            weight.sort(reverse=True)
            for i in range(len(weight)):
                if totalApples <= 5000:
                    return len(weight[i::])
                totalApples -= weight[i]

        return len(weight)
