from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multi sourced bfs 
        row = len(grid)
        col = len(grid[0])
        q = deque() # stores [loc, dist]
        INF = 2147483647

        # add all treasure points
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append([(i, j), 0])
        
        # then use bfs to traverse them 
        dr = [0 , 0, -1, 1]
        dc = [1, -1, 0, 0]

        while q:
            curr, dist = q.popleft()
            r, c = curr
    
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if (nr < 0 or nc < 0 or nr >= row or nc >= col or grid[nr][nc] != INF):
                    continue
                q.append([(nr, nc), dist+1])
                grid[nr][nc] = dist+1
            
        # return grid


