class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        i = 0
        while l <= r and i <= r:
            if nums[i] == 0:
                nums[i] = nums[l]
                nums[l] = 0
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i] = nums[r]
                nums[r] = 2
                r -= 1
            else:
                i += 1
