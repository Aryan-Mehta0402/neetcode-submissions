class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1]*len(nums)
        suffix_prod = [1]*len(nums)

        prod = 1
        for i in range(len(nums)):
            prefix_prod[i] = prod
            prod *= nums[i]
        print(prefix_prod)
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            suffix_prod[i] = prod
            prod *= nums[i]
        print(suffix_prod)
        result = [x * y for x, y in zip(prefix_prod, suffix_prod)]
        return result
