class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        n = len(nums)

        def rec(i, summ):
            if i == n:
                if summ == target:
                    return 1
                else: 
                    return 0

            if (i, summ) in dp:
                return dp[(i, summ)]

            dp[(i, summ)] = rec(i+1, summ + nums[i]) + rec(i+1, summ - nums[i])
            return dp[(i, summ)]

        return rec(0, 0)