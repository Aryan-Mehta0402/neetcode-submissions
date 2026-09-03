class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        xor = 0
        for i in range(len(nums)+1):
            if i != len(nums):
                xor ^= nums[i]
            ans ^= i

        return ans^xor