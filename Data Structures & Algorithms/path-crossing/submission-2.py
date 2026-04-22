class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pathMap = {"N": (0, 1), "E": (1,0), "S": (0,-1), "W": (-1, 0)}
        x, y = 0, 0
        visited = {(0, 0)}
        for p in path:
            dx, dy = pathMap[p]
            x += dx
            y += dy
            if (x,y) in visited:
                return True
            visited.add((x, y))
        return False

