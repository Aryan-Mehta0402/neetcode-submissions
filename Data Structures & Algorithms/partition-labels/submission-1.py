class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # get each character and make a map
        # ch - (l, r) now apply greedy like time scheduling?
        st = 0
        end = 0
        res = []
        mapp = {}

        for i, ch in enumerate(s):
            mapp[ch] = i

        for i, ch in enumerate(s):
            end = max(end, mapp[ch])

            if i == end:
                res.append(end-st+1)
                st = i + 1

        return res