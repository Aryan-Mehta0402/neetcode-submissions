class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # get each character and make a map
        # ch - (l, r) now apply greedy like time scheduling?
        mapp = {}

        for i, ch in enumerate(s):
            if ch not in mapp:
                mapp[ch] = [i, i]
            else:
                mapp[ch][1] = i

        l = 0
        r = 0
        res = []

        for i in range(len(s)):
            r = max(r, mapp[s[i]][1])

            if i == r:
                res.append(r-l+1)
                l = r+1

        return res