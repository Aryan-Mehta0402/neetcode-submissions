class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        opp = "({["
        dicti = {"}" : "{", ")": "(", "]": "["}
        if len(s)%2 == 1:
            return False 

        for i in range(len(s)):
            if s[i] in opp:
                stk.append(s[i])
            else:
                if (len(stk) > 0) and (dicti[s[i]] == stk[-1]):
                    stk.pop()
                else:
                    return False

        if len(stk) == 0:
            return True
        return False