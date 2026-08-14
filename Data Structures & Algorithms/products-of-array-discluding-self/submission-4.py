class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = [1]*len(nums)
        for i in range(1, len(nums)):
            pre_prod[i] = pre_prod[i-1]*nums[i-1]
 
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            curr = nums[i]
            nums[i] = prod
            prod *= curr
            nums[i] = pre_prod[i]*nums[i]

        return nums