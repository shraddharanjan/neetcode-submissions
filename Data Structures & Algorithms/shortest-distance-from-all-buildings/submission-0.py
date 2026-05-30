class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        total_houses = 0

        distances = [[[0, 0] for _ in range(cols)] for _ in range(rows)]

        def bfs(start_row, start_col):
            q = deque([(start_row, start_col)])
            vis = [[False] * cols for _ in range(rows)]
            vis[start_row][start_col] = True
            steps = 0

            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()

                    if grid[row][col] == 0:
                        distances[row][col][0] += steps
                        distances[row][col][1] += 1

                    for dr, dc in dirs:
                        next_row, next_col = row + dr, col + dc
                        if 0 <= next_row < rows and 0 <= next_col < cols:
                            if not vis[next_row][next_col] and grid[next_row][next_col] == 0:
                                vis[next_row][next_col] = True
                                q.append((next_row, next_col))
                steps += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    total_houses += 1
                    bfs(row, col)

        min_distance = float('inf')
        for row in range(rows):
            for col in range(cols):
                if distances[row][col][1] == total_houses:
                    min_distance = min(min_distance, distances[row][col][0])

        return -1 if min_distance == float('inf') else min_distance