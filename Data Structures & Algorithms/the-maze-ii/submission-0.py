class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        distance = [[float('inf')] * len(maze[0]) for _ in range(len(maze))]
        distance[start[0]][start[1]] = 0
        self.dijkstra(maze, start, distance)
        return -1 if distance[destination[0]][destination[1]] == float('inf') else distance[destination[0]][destination[1]]

    def dijkstra(self, maze: List[List[int]], start: List[int], distance: List[List[int]]) -> None:
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        queue = []
        heapq.heappush(queue, (0, start[0], start[1]))  # (distance, x, y)

        while queue:
            dist, sx, sy = heapq.heappop(queue)

            if distance[sx][sy] < dist:
                continue

            for dx, dy in dirs:
                x, y = sx + dx, sy + dy
                count = 0

                while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                    x += dx
                    y += dy
                    count += 1

                if distance[sx][sy] + count < distance[x - dx][y - dy]:
                    distance[x - dx][y - dy] = distance[sx][sy] + count
                    heapq.heappush(queue, (distance[x - dx][y - dy], x - dx, y - dy))