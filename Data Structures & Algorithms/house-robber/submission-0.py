class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        dp = [0]*n
        dp[n-2] = nums[n-2]

        for i in range(n-3, -1, -1):
            dp[i] = nums[i] + max(dp[i+2:])

        return max(dp)