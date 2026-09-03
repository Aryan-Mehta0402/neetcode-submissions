class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans += (2**(31 - i))*(n & 1)
            n >>= 1
        return ans
        