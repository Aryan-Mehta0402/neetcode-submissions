class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        while l < r:

            # current range already sorted
            if nums[l] < nums[r]:
                return nums[l]

            m = (l + r) // 2

            # minimum lies on right side
            if nums[m] > nums[r]:
                l = m + 1

            # minimum lies at m or left side
            else:
                r = m

        return nums[l]