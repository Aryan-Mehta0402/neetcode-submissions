class Solution:
    def climbStairs(self, n: int) -> int:

        prev = 1
        curr = 1

        for i in range(n-1):
            curr, prev = curr+prev, curr

        return curr


        