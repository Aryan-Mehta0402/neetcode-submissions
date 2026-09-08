from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        q = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    grid[i][j] = -1 # easy to check for fresh fruit
                elif grid[i][j] == 2:
                    q.append([(i, j), 0])
                    grid[i][j] = 0

        while q:
            curr, dist = q.popleft()
            i, j = curr
            dr = [0, 0, -1, 1]
            dc = [1, -1, 0, 0]

            for k in range(4):
                nr, nc = i + dr[k], j + dc[k]
                if nr < 0 or nc < 0 or nr >= row or nc >= col or grid[nr][nc] != -1:
                    continue
                q.append([(nr, nc), dist+1])
                grid[nr][nc] = dist + 1
        
        maxx = 0
        print(grid)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == -1:
                    return -1
                maxx = max(maxx, grid[i][j])

        return maxx