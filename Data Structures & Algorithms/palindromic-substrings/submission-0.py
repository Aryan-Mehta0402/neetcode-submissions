class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        # for odd length
        for i in range(len(s)):
            for j in range(0, i+1):
                if i+j >= len(s):
                    break
                
                if s[i-j] == s[i+j]:
                    res += 1
                else:
                    break

        # for even length
        for i in range(len(s)-1):
            for j in range(i + 1):
                if i - j < 0 or i + j + 1 >= len(s):
                    break

                if s[i - j] == s[i + j + 1]:
                    res += 1
                else:
                    break

        return res