class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mapp = {"{": "}", "[": "]", "(": ")"}

        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stk.append(s[i])
            else:
                if not stk:
                    return False
                if s[i] == mapp[stk[-1]]:
                    stk.pop()
                else:
                    return False

        return not stk