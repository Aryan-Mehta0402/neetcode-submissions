class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        used = [False] * len(nums)

        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])
                return

            for j in range(len(nums)):
                if used[j]:
                    continue

                used[j] = True
                sol.append(nums[j])

                backtrack()

                sol.pop()
                used[j] = False

        backtrack()
        return res