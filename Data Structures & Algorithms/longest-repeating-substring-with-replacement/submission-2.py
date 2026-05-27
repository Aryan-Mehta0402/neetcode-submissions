class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        leng = 1
        counte = {}

        for r in range(len(s)):
            counte[s[r]] = 1 + counte.get(s[r], 0)

            while (r-l+1) - max(counte.values()) > k:
                counte[s[l]] -= 1
                l += 1

            leng = r-l+1   
            max_len = max(max_len, leng)
        return max_len