from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        M = defaultdict(list)
        visited = set()

        for u, v in prereq:
            M[u].append(v) # prereq of u is v

        def dfs(c, v):
            if c in v: return False # cycle exists
            if c in visited: return True # prev explored node so can never have cycle

            v.add(c)

            ans = True
            for n in M[c]:
                ans &= dfs(n, v)

            v.remove(c)
            visited.add(c)

            return ans

        ans = True
        for i in range(numCourses):
            visiting = set()
            ans &= dfs(i, visiting)
        return ans
        