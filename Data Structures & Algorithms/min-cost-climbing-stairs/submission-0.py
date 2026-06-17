class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 2 starts
        # max(2 options)
        n = len(cost)
        dp = [0]*n

        for j in range(n-1, -1, -1):
            if j+1 >= n or j+2 >= n:
                dp[j] = cost[j]
                continue
            dp[j] = cost[j]+min(dp[j+1], dp[j+2])

        return min(dp[0], dp[1])
