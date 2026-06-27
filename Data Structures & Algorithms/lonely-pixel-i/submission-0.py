class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        # Returns true if the cell at (x, y) is lonely.
        # There should not be any other black cell
        # In the first row and column except (x, y) itself.
        def check(x, y):
            n = len(picture)
            m = len(picture[0])

            cnt = 0
            for i in range(n):
                cnt += 1 if picture[i][y] == 'B' else 0

            for j in range(m):
                # avoid double count (x, y)
                if j != y:
                    cnt += 1 if picture[x][j] == 'B' else 0

            return picture[x][y] == 'B' and cnt == 1

        n = len(picture)
        m = len(picture[0])

        answer = 0
        for j in range(m):
            answer += 1 if check(0, j) else 0

        for i in range(1, n):
            answer += 1 if check(i, 0) else 0

        # Convert cell 'B' to '1' and 'W' to '0'
        for j in range(m):
            picture[0][j] = '1' if picture[0][j] == 'B' else '0'

        for i in range(n):
            picture[i][0] = '1' if picture[i][0] == 'B' else '0'

        # If the cell is black increment the count of corresponding row and column by 1
        for i in range(1, n):
            for j in range(1, m):
                if picture[i][j] == 'B':
                    picture[i][0] = chr(ord(picture[i][0]) + 1)
                    picture[0][j] = chr(ord(picture[0][j]) + 1)

        for i in range(1, n):
            for j in range(1, m):
                if picture[i][j] == 'B':
                    if picture[0][j] == '1' and picture[i][0] == '1':
                        answer += 1

        return answer