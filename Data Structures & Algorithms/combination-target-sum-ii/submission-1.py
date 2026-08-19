class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        nums.sort()

        def backtrack(i):
            if sum(sol) > target:
                return

            if sum(sol) == target: 
                res.append(sol[:])
                return

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                sol.append(nums[j])
                backtrack(j+1)
                sol.pop()

        backtrack(0)
        return res