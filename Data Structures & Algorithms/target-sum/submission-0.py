class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        n = len(nums)

        def rec(i, rem):
            if i == n:
                if rem == target:
                    return 1
                else:
                    return 0

            if (i, rem) in dp:
                return dp[(i, rem)]

            dp[(i, rem)] = rec(i+1, rem - nums[i]) + rec(i+1, rem + nums[i])
            return dp[(i, rem)]

        return rec(0, 0)