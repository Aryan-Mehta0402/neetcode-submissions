class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        max_l = 0

        if len(s) < 2:
            return len(s)

        string = s[l]
        max_l = 1

        while r < len(s):

            if s[r] in string:
                l = l + string.index(s[r]) + 1
                string = s[l:r+1]

            else:
                string += s[r]

            max_l = max(max_l, len(string))
            r += 1

        return max_l