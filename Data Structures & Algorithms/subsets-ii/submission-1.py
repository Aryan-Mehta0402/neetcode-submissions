class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        sol = []

        def rec(i):
            res.append(sol[:])
        
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                sol.append(nums[j])
                rec(j+1)
                sol.pop()

        rec(0)
        return res
