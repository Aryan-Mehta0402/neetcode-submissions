class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c, d = 0, 1, 1, 2
        if n == 0:
            return a
        if n == 1 or n == 2:
            return 1
        for i in range(3, n):
            a = b
            b = c
            c = d
            d = a + b + c
        return d