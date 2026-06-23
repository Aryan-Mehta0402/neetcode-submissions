class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text2)
        n = len(text1)

        dp = [[-1]*(m+1) for _ in range(n+1)]

        def rec(i, j):
            if j >= m:
                return 0
            if i >= n:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] = 1 + rec(i+1, j+1)
                return dp[i][j]
            
            dp[i][j] = max(rec(i,j+1), rec(i+1,j))
            return dp[i][j]

        return rec(0,0)