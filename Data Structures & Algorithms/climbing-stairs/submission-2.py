class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n 

        prev = 1
        curr = 2

        for i in range(n-2):
            prev, curr = curr, prev+curr
# 1, 2, 3, 5
        return curr