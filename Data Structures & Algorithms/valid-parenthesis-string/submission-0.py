class Solution:
    def checkValidString(self, s: str) -> bool:
        cnt_l = 0
        cnt_r = 0
        cnt_s = 0

        for i in range(len(s)):
            if s[i] == "(":
                cnt_l += 1
            elif s[i] == ")":
                cnt_r += 1
            else:
                cnt_s += 1

        if abs(cnt_r - cnt_l) > cnt_s:
            return False
        left = []
        star = []
        for i, ch in enumerate(s):
            if ch == '(':
                left.append(i)
            elif ch == '*':
                star.append(i)
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()

        while left and star:
            if left.pop() > star.pop():
                return False
        return not left
        
        return True