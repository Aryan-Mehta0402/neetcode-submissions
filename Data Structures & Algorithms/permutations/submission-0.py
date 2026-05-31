class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # have a hash map to check for the element

        res = []
        sol = []

        def backtrack(i):
            # base case
            if i == len(nums):
                res.append(sol[:])
                return

            for j in range(len(nums)):
                if nums[j] in sol:
                    continue
                else:
                    sol.append(nums[j])
                    backtrack(i+1)
                    sol.pop()
    
        backtrack(0)
        return res