class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # longest inc subseq
        # f(i) = 1 + max(all f(j) such that nums[j] > nums[i])
        n = len(nums)
        dp = [0]*(n+1)
        dp[n] = 1

        def rec(i):
            if dp[i] != 0:
                return dp[i]

            if i == n: return dp[n]

            dp[i] = 1 + max((rec(x) for x in range(i+1, n) if nums[x] > nums[i]), default = 0)
            return dp[i]
        
        return max(rec(i) for i in range(n))