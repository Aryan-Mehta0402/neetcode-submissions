class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # start traversing from treasure and do bfs from there
        # as it will be easy to maintain the distance
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        dist = 1
        inf = 2147483647

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                dirx = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in dirx:
                    r, c = row + dr, col + dc
                    if -1 < r < rows and -1 < c < cols:
                        if grid[r][c] == -1 or grid[r][c] == 0:
                            continue
                        if grid[r][c] == inf:
                            q.append((r, c))
                            grid[r][c] = dist
                    else:
                        continue

            dist += 1
