class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        maxx = -1*float("inf")
        if len(nums) == 1:
            return nums[0]
        # what if all elements of array are negative
        for i in range(len(nums)):
            summ += nums[i]
            maxx = max(summ, maxx)
            if summ < 0:
                summ = 0

        return maxx
            
        
            