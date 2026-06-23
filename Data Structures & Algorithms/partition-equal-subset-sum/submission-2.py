class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # if sum is odd return false
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]

        if sum%2 == 1:
            return False

        dp = [[-1] * (sum//2 + 1) for _ in range(len(nums)+1)]

        def rec(index, target):
    
            if target == 0:
                return True
            if index == len(nums) or target < 0:
                return False

            if dp[index][target] != -1:
                return dp[index][target]

            dp[index][target] = (
                rec(index + 1, target - nums[index]) or
                rec(index + 1, target)
            )

            return dp[index][target]

        return rec(0, sum//2)
