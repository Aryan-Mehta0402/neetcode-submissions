class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()
        peri = 0

        def dfs(i, j):
            nonlocal peri

            if i < 0 or i >= row or j < 0 or j >= col:
                return 
            if grid[i][j] == 0:
                visited.add((i, j))
                return
            if (i, j) in visited:
                return
            
            visited.add((i, j))
            dr = [0, 0, -1, 1]
            dc = [1, -1, 0, 0]

            for k in range(4):
                if i+dr[k] < 0 or i+dr[k] >= row or j+dc[k] < 0 or j+dc[k] >= col:
                    peri += 1
                elif grid[i+dr[k]][j+dc[k]] == 1:
                    pass
                else: 
                    peri += 1

            for k in range(4):
                if (i+dr[k], j+dc[k]) not in visited:
                    dfs(i+dr[k], j+dc[k])


        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return peri