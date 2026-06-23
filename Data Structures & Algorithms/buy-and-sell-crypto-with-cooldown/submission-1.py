class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)

        def rec(i, buy):
            if i >= n:
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]

            cooldown = rec(i+1, buy)
            if buy:
                buys = rec(i+1, not buy) - nums[i]
                dp[(i, buy)] = max(buys, cooldown)
            else:
                sell = rec(i+2, not buy) + nums[i]
                dp[(i, buy)] = max(sell, cooldown)
            return dp[(i, buy)]

        return rec(0, True)