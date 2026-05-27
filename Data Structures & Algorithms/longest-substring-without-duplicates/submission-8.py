class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_l = 0
        charset = set()

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            max_l = max(r-l+1, max_l) 
        return max_l
