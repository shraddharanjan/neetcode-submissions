class Excel:

    def __init__(self, height: int, width: str):
        self.formulas = [[None] * (ord(width) - ord('A') + 1) for _ in range(height)]
        self.stack = []

    def set(self, row: int, column: str, val: int) -> None:
        self.formulas[row - 1][ord(column) - ord('A')] = ({}, val)
        self.topological_sort(row - 1, ord(column) - ord('A'))
        self.execute_stack()

    def get(self, row: int, column: str) -> int:
        cell = self.formulas[row - 1][ord(column) - ord('A')]
        if cell is None:
            return 0
        return cell[1]

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        cells = self.convert(numbers)
        summ = self.calculate_sum(row - 1, ord(column) - ord('A'), cells)
        self.set(row, column, summ)
        self.formulas[row - 1][ord(column) - ord('A')] = (cells, summ)
        return summ

    def topological_sort(self, r: int, c: int):
        for i in range(len(self.formulas)):
            for j in range(len(self.formulas[0])):
                if self.formulas[i][j] is not None and (chr(ord('A') + c) + str(r + 1)) in self.formulas[i][j][0]:
                    self.topological_sort(i, j)
        self.stack.append((r, c))

    def execute_stack(self):
        while self.stack:
            top = self.stack.pop()
            if len(self.formulas[top[0]][top[1]][0]) > 0:
                self.calculate_sum(top[0], top[1], self.formulas[top[0]][top[1]][0])

    def convert(self, strs: List[str]) -> dict:
        res = {}
        for st in strs:
            if ':' not in st:
                res[st] = res.get(st, 0) + 1
            else:
                parts = st.split(':')
                si = int(parts[0][1:])
                ei = int(parts[1][1:])
                sj = parts[0][0]
                ej = parts[1][0]
                for i in range(si, ei + 1):
                    j = sj
                    while j <= ej:
                        key = j + str(i)
                        res[key] = res.get(key, 0) + 1
                        j = chr(ord(j) + 1)
        return res

    def calculate_sum(self, r: int, c: int, cells: dict) -> int:
        total = 0
        for s, count in cells.items():
            x = int(s[1:]) - 1
            y = ord(s[0]) - ord('A')
            total += (self.formulas[x][y][1] if self.formulas[x][y] is not None else 0) * count
        self.formulas[r][c] = (cells, total)
        return total


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
