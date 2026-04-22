class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, k):

            if k == 0:
                res.append(cur.copy())
                return   
            if i > n:
                return 

            cur.append(i)
            dfs(i + 1, cur, k - 1)
            cur.pop()
            dfs(i + 1, cur, k)
        dfs(1, [], k)
        return res

