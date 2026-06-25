class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        maxx = min(nums) - 1

        for i in range(len(nums)):
            if prefix < 0:
                prefix = 0
            prefix += nums[i]
            maxx = max(maxx, prefix)

        return maxx
            