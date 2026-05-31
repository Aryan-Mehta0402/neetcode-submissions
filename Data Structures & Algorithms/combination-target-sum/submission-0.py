class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        nums.sort()

        def backtrack(i):
            if sum(sol) > target:
                return
            elif sum(sol) < target:
                for j in range(i, len(nums)):
                    sol.append(nums[j])
                    backtrack(j)
                    sol.pop()
            else: 
                res.append(sol[:])
                return

        backtrack(0)
        return res
            