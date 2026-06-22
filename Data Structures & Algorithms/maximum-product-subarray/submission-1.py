class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        maxx = min(nums) - 1

        for i in range(len(nums)):
            if prefix == 0:
                prefix = 1
            prefix *= nums[i]
            maxx = max(maxx, prefix)

        for i in range(len(nums)-1,-1,-1 ):
            if suffix == 0:
                suffix = 1
            suffix *= nums[i]
            maxx = max(maxx, suffix)

        return maxx