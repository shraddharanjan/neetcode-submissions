class Solution:
    def _backtracking(self, factors: List[int], ans: List[List[int]]) -> None:
        # Got a solution.
        if len(factors) > 1:
            ans.append(factors.copy())

        last_factor = factors.pop()

        i = 2 if not factors else factors[-1]
        while i <= last_factor // i:
            if last_factor % i == 0:
                # Add i and last_factor // i.
                factors.append(i)
                factors.append(last_factor // i)
                self._backtracking(factors, ans)
                # Remove the last 2 elements in factors to restore it after the recursion returns.
                factors.pop()
                factors.pop()
            i += 1

        # Add last_factor back to factors to restore it.
        factors.append(last_factor)

    def getFactors(self, n: int) -> List[List[int]]:
        ans = []
        self._backtracking([n], ans)
        return ans