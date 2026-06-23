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

            if dp[index+1][target-nums[index]] != -1:
                way1 = dp[index+1][target-nums[index]]
            else:
                way1 = rec(index+1, target-nums[index])
                dp[index+1][target-nums[index]] = way1

            if dp[index+1][target] != -1:
                way2 = dp[index+1][target]
            else:
                way2 = rec(index+1, target)
                dp[index+1][target] = way2

            return way1 or way2

        return rec(0, sum//2)
