class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        stk = []
        ma = 0

        for i in range(len(h)):

            if len(stk) == 0:
                stk.append([i, h[i]])
                continue

            if h[i] == stk[-1][1]:
                continue

            if h[i] > stk[-1][1]:
                stk.append([i, h[i]])

            else:
                while stk and (h[i] < stk[-1][1]):

                    idx, ht = stk[-1]

                    ma = max(ma, ht * (i - idx))

                    prvi = idx
                    stk.pop()

                stk.append([prvi, h[i]])

        for idx, ht in stk:
            ma = max(ma, ht * (len(h) - idx))

        return ma