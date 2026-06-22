class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1]*(n) # boolean
        mlen = 0

        for i in range(len(wordDict)):
            mlen = max(mlen, len(wordDict[i]))

        wordDict = set(wordDict)

        def rec(prev_index, index):
            if index == n:
                dp[prev_index] = True
                return True

            if dp[index] != -1:
                return dp[index]

            for i in range(index, min(n, index+mlen)):
                if s[index:i+1] in wordDict:
                    res = rec(index, i+1)
                    if res == True:
                        dp[index] = True
                        return True
            dp[index] = False
            return False

        return rec(0, 0)
