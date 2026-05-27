class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_set = {}
        sub_set = {}

        for ch in s1:
            s1_set[ch] = 1 + s1_set.get(ch, 0)

        l = 0

        for r in range(len(s2)):

            sub_set[s2[r]] = 1 + sub_set.get(s2[r], 0)

            # shrink window if size exceeds len(s1)
            if (r - l + 1) > len(s1):
                sub_set[s2[l]] -= 1

                if sub_set[s2[l]] == 0:
                    del sub_set[s2[l]]

                l += 1

            # compare frequency maps
            if sub_set == s1_set:
                return True

        return False