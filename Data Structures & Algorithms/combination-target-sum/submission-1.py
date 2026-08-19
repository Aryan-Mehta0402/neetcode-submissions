class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []

        def rec(i, summ):

            if summ == target:
                res.append(sol[:])
                return

            if i == len(nums) or summ > target:
                return

            rec(i+1, summ)

            sol.append(nums[i])
            rec(i, summ + nums[i])
            sol.pop()

        rec(0, 0)
        return res
            