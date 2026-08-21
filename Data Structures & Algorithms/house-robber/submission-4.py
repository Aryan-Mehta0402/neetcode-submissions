class Solution:
    def rob(self, nums: List[int]) -> int:
        # let rob[i] = max amount robbed starting ffrom index i

        n = len(nums)
        nums[n-2] = max(nums[n-2], nums[n-1])

        for i in range(n-3,-1,-1):
            nums[i] = max(nums[i] + nums[i+2], nums[i+1])

        return nums[0]
