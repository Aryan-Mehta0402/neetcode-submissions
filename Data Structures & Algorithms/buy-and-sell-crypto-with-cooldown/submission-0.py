class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n+1)

        def rec(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]

            dp[i] = max(rec(i+1), 
                        max((nums[x] - nums[i] + rec(x+2) 
                        for x in range(i+1,n) 
                        if nums[x] > nums[i]), default=0))
            return dp[i]

        return rec(0)