class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        dp = [0]*n
        dp[n-2] = nums[n-2]

        for i in range(n-3, -1, -1):
            dp[i] = max(nums[i]+dp[i+2], dp[i+1])

        return max(dp)