class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp[i] = min num of jumps to get from i to end
        n = len(nums)
        dp = [0]*n

        for i in range(n-2, -1, -1):
            if nums[i] == 0:
                dp[i] = float("inf")
                continue
            if i + nums[i] >= n - 1:
                dp[i] = 1
            else:
                dp[i] = 1 + min(dp[i + 1:i + nums[i] + 1])
                
        return dp[0]