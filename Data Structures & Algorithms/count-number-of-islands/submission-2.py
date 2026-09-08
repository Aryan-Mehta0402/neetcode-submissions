class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row = len(grid)
        col = len(grid[0])
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j >= col:
                return False
            if (i, j) in visited:
                return False
            if grid[i][j] == "0":
                return False

            visited.add((i, j))
            dr = [0, 0, 1, -1]
            dc = [1, -1, 0, 0]

            for k in range(4):
                dfs(i+dr[k], j+dc[k])
            
            return True

        for i in range(row):
            for j in range(col):
                if dfs(i, j):
                    count += 1
        return count
