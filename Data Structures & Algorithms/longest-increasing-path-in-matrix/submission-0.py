class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[-1]*cols for _ in range(rows)]

        def rec(i, j):
            if i < 0 or i > rows or j < 0 or j > cols:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = 1 + max(
                                (
                                    rec(ni, nj)
                                    for ni, nj in (
                                        (i - 1, j),
                                        (i + 1, j),
                                        (i, j - 1),
                                        (i, j + 1),
                                    )
                                    if 0 <= ni < rows
                                    and 0 <= nj < cols
                                    and matrix[ni][nj] > matrix[i][j]
                                ),
                                default=0,
                            )

            return dp[i][j]


        for i in range(rows):
            for j in range(cols):
                rec(i, j)

        return max(max(row) for row in dp)
