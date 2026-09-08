class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        R, C = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= R or j >= C or grid[i][j] != "O":
                return

            grid[i][j] = "T"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Border O's
        for i in range(R):
            dfs(i, 0)
            dfs(i, C - 1)

        for j in range(C):
            dfs(0, j)
            dfs(R - 1, j)

        # Capture surrounded O's and restore safe O's
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "O":
                    grid[i][j] = "X"
                elif grid[i][j] == "T":
                    grid[i][j] = "O"