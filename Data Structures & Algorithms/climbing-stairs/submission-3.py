class Solution:
    def climbStairs(self, n: int) -> int:

        # dp[i] = number of ways to reach n from state i
        # need to find dp[0]
        # dp[i] = dp[i+1] + dp[i+2]
        # dp[i-1] = dp[i] + dp[i+1]
        if n <= 2:
            return n
        a, b, c = 2, 1, 1
        for i in range(n-3, -1, -1):
            c = b
            b = a
            a = b + c

        return a
