from collections import defaultdict
import copy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)
        ans = []
        d = copy.deepcopy(strs)

        for i in range(len(strs)):
            strs[i] = tuple(sorted(strs[i]))
            mapp[strs[i]].append(i)

        for key in mapp:
            res = [d[j] for j in mapp[key]]
            ans.append(res)

        return ans

            


