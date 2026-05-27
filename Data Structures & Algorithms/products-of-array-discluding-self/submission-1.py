class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix_prod = [1]*len(nums)
        # suffix_prod = [1]*len(nums)
        result = [1]*len(nums)
        prod = 1
        for i in range(len(nums)):
            result[i] = prod
            prod *= nums[i]
        print(result)
        
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= prod
            prod *= nums[i]
        print(result)
        
        # result = [x * y for x, y in zip(prefix_prod, suffix_prod)]
        return result
