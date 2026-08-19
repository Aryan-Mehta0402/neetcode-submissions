class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def rec(i):
            if i == len(nums):
                res.append(sol[:])
                return 

            rec(i+1)

            sol.append(nums[i])
            rec(i+1)
            sol.pop()

        rec(0)
        return res