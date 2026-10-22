class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def rob_linear(arr):
            prev1 = 0
            prev2 = 0

            for num in arr:
                prev1, prev2 = max(prev2 + num, prev1), prev1

            return prev1

        return max(
            rob_linear(nums[:-1]),  # exclude last
            rob_linear(nums[1:])    # exclude first
        )