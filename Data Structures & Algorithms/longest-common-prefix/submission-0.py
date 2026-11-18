class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        ans = strs[0]

        for i in range(1, len(strs)):
            prefix = ""
            for ch1, ch2 in zip(ans, strs[i]):
                if ch1 == ch2:
                    prefix += ch1
                else:
                    ans = prefix
                    break
        return ans