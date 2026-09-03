class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        a &= mask
        b &= mask

        if (a & b) == 0:
            result = a ^ b
        else:
            result = self.getSum(
                ((a & b) << 1) & mask,
                (a ^ b) & mask
            )

        if result > max_int:
            return ~(result ^ mask)

        return result
