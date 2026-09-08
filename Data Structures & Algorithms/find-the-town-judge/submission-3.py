from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        M = defaultdict(list) # who trusts a 
        V = defaultdict(list) # who a trusts

        cnt = 0
        ans = -1

        for u, v in trust:
            M[v].append(u)
            V[u].append(v)

        for a in M:
            if len(M[a]) == n-1 and len(V[a]) == 0:
                cnt += 1
                ans = a
            if cnt > 1:
                return -1
        return ans