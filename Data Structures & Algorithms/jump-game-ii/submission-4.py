class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp[i] = min num of jumps to get from i to end
        n = len(nums)
        r = 0
        jumps = 0
        l = 0

        for i in range(n-1):
            r = max(r, i + nums[i])
            if l == i:
                l = r
                jumps += 1
                
        return jumps