class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # f(i,j) = 1 + f(i+1,j) + f(i, j+1) # if possible to go right and down
        dp = [[-1]*n for _ in range(m)]

        def rec(i, j):

            if dp[i][j] != -1:
                return dp[i][j]
                 
            if i == m-1:
                dp[i][j] = 1
                return dp[i][j]

            if j == n-1:
                dp[i][j] = 1
                return dp[i][j]

            dp[i][j] = rec(i+1,j) + rec(i, j+1)

            return dp[i][j]
        rec(0, 0)
        return dp[0][0]