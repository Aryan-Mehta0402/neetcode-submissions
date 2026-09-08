class Solution:
    def solve(self, grid: List[List[str]]) -> None:    
        # start from all the O's connected borders and change all the others
        row = len(grid)
        col = len(grid[0])
        visited = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == "X": return
            if (i, j) in visited: return
            visited.add((i, j))
            dr = [0, 0, 1, -1]
            dc = [1, -1, 0, 0]

            for k in range(4):
                nr, nc = i + dr[k], j + dc[k]
                dfs(nr, nc)

        for i in range(row): # 1st col
            if grid[i][0] == "O":
                dfs(i , 0)

        for i in range(row): # last col
            if grid[i][col-1] == "O":
                dfs(i , col-1)

        for i in range(col): # 1st row
            if grid[0][i] == "O":
                dfs(0, i)

        for i in range(col): # last row
            if grid[row-1][i] == "O":
                dfs(row-1 , i)

        for i in range(row):
            for j in range(col):
                if (i, j) in visited:
                    continue
                grid[i][j] = "X"
