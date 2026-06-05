class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        ma = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            area = 1

            while q:
                row, col = q.popleft()
                dirx = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in dirx:
                    r, c = row+dr, col+dc
                    if  (-1 < r < rows and
                        -1 < c < cols and
                        grid[r][c] == 1 and
                        (r, c) not in visited):

                        visited.add((r, c))
                        q.append((r, c))
                        area += 1

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    visited.add((r, c)) 
                    ma = max(bfs(r, c), ma)

        return ma

        