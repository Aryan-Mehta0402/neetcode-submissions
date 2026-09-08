class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxx = 0
        row = len(grid)
        col = len(grid[0])
        # set to 0 instead of using visited

        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j >= col:
                return 0
            if grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            dr = [0, 0, -1, 1]
            dc = [1, -1, 0, 0]

            area = 1
            for k in range(4):
                area += dfs(i+dr[k], j+dc[k])
            
            return area

        for i in range(row):
            for j in range(col):
                maxx = max(maxx, dfs(i, j))

        return maxx