class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()

        def dfs(t, start, sol):
            if t == 0:
                ans.append(sol.copy())
                return

            for i in range(start, len(nums)):
                if nums[i] > t:
                    break

                sol.append(nums[i])
                dfs(t - nums[i], i, sol)  # i allows reuse
                sol.pop()

        dfs(target, 0, [])
        return ans