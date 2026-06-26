class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # compute sum
        n = len(nums)
        summ = n*(n+1)//2
        summa = 0

        for i in range(n):
            summa += nums[i]

        return summ - summa