class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        n, m = len(image), len(image[0])

        dirs = (1, 0, -1, 0, 1)
        def dfs(r, c, org):
            if not (0 <= r < n) or not (0 <= c < m) or image[r][c] != org:
                return
            image[r][c] = color
            for d in range(4):
                dfs(r + dirs[d], c + dirs[d + 1], org) 
        dfs(sr, sc, image[sr][sc])
        return image
