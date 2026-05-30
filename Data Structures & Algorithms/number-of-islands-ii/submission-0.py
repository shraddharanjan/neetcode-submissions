class UnionFind:
    def __init__(self, size):
        self.parent = [-1] * size
        self.rank = [0] * size
        self.count = 0

    def add_land(self, x):
        if self.parent[x] >= 0:
            return
        self.parent[x] = x
        self.count += 1

    def is_land(self, x):
        if self.parent[x] >= 0:
            return True
        else:
            return False

    def number_of_islands(self):
        return self.count

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)

        if xset == yset:
            return
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1

        self.count -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]
        dsu = UnionFind(m * n)
        answer = []

        for position in positions:
            land_position = position[0] * n + position[1]
            dsu.add_land(land_position)

            for i in range(4):
                neighbor_x = position[0] + x[i]
                neighbor_y = position[1] + y[i]
                neighbor_position = neighbor_x * n + neighbor_y

                # If neighborX and neighborY correspond to a point in the grid and there is a
                # land at that point, then merge it with the current land.
                if neighbor_x >= 0 and neighbor_x < m and neighbor_y >= 0 and neighbor_y < n and dsu.is_land(neighbor_position):
                    dsu.union(land_position, neighbor_position)

            answer.append(dsu.number_of_islands())

        return answer